#!/usr/bin/env python3
"""
Build species albums, thumbnails, EXIF, and stable like metadata.
Place images inside photo_gallery/<species>/ and run this script.
Run this whenever you add new photos:  python3 scripts/extract_gallery_exif.py
"""
import hashlib
import json
import os
import re
import struct
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO_DIR = os.path.join(REPO_ROOT, 'photo_gallery')


def _read_rational(data, offset, bo):
    num = struct.unpack_from(bo + 'I', data, offset)[0]
    den = struct.unpack_from(bo + 'I', data, offset + 4)[0]
    return num / den if den else None


def _read_ifd(data, tiff_start, ifd_offset, bo, needed_tags):
    try:
        num = struct.unpack_from(bo + 'H', data, tiff_start + ifd_offset)[0]
    except Exception:
        return {}
    result = {}
    for j in range(num):
        try:
            entry = tiff_start + ifd_offset + 2 + j * 12
            tag   = struct.unpack_from(bo + 'H', data, entry)[0]
            type_ = struct.unpack_from(bo + 'H', data, entry + 2)[0]
            count = struct.unpack_from(bo + 'I', data, entry + 4)[0]
            ob    = data[entry + 8: entry + 12]
        except Exception:
            continue
        if tag not in needed_tags:
            continue
        if type_ == 2:  # ASCII
            if count <= 4:
                val = ob[:count].rstrip(b'\x00').decode('latin-1', errors='replace')
            else:
                ptr = struct.unpack_from(bo + 'I', ob)[0]
                val = data[tiff_start + ptr: tiff_start + ptr + count].rstrip(b'\x00').decode('latin-1', errors='replace')
        elif type_ == 3:  # SHORT
            val = struct.unpack_from(bo + 'H', ob)[0] if count == 1 else (
                struct.unpack_from(bo + 'H', data, tiff_start + struct.unpack_from(bo + 'I', ob)[0])[0])
        elif type_ == 4:  # LONG
            val = struct.unpack_from(bo + 'I', ob)[0]
        elif type_ == 5:  # RATIONAL
            ptr = struct.unpack_from(bo + 'I', ob)[0]
            val = _read_rational(data, tiff_start + ptr, bo)
        else:
            continue
        result[needed_tags[tag]] = val
    return result


IFD0_TAGS = {0x010F: 'Make', 0x0110: 'Model', 0x8769: '_ExifIFD'}
EXIF_TAGS = {
    0x829A: 'ExposureTime',
    0x829D: 'FNumber',
    0x8827: 'ISO',
    0x920A: 'FocalLength',
    0xA434: 'LensModel',
    0x9003: 'DateTimeOriginal',
}


def extract_exif(path):
    if Path(path).suffix.lower() not in {'.jpg', '.jpeg'}:
        with Image.open(path) as image:
            exif = image.getexif()
            tags = {name: exif[tag] for tag, name in IFD0_TAGS.items()
                    if tag in exif and name != '_ExifIFD'}
            detail = exif.get_ifd(0x8769)
            tags.update({name: detail[tag] for tag, name in EXIF_TAGS.items() if tag in detail})
            return tags
    with open(path, 'rb') as f:
        data = f.read()
    if data[:2] != b'\xff\xd8':
        return None
    i = 2
    while i < len(data) - 3:
        if data[i] != 0xff:
            break
        marker = data[i + 1]
        length = struct.unpack_from('>H', data, i + 2)[0]
        if marker == 0xe1:
            seg = data[i + 4: i + 2 + length]
            if seg[:6] == b'Exif\x00\x00':
                tiff = seg[6:]
                bo = '<' if tiff[:2] == b'II' else '>'
                ifd0_off = struct.unpack_from(bo + 'I', tiff, 4)[0]
                tags = _read_ifd(tiff, 0, ifd0_off, bo, IFD0_TAGS)
                exif_off = tags.pop('_ExifIFD', None)
                if exif_off:
                    tags.update(_read_ifd(tiff, 0, exif_off, bo, EXIF_TAGS))
                return tags
        i += 2 + length
    return None


def format_shutter(s):
    if s is None:
        return None
    if s >= 1:
        return str(round(s, 1)) + 's'
    return '1/' + str(round(1 / s))


def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    serialized = json.dumps(data, indent=2, ensure_ascii=False)
    temporary = Path(str(path) + '.tmp')
    temporary.write_text(serialized + '\n', encoding='utf-8')
    temporary.replace(path)


def fingerprint_file(path):
    digest = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def slugify_counter_name(name):
    slug = re.sub(r'[^0-9A-Za-z]+', '-', name).strip('-').lower()
    return slug or 'photo'


def normalize_like_meta_entry(entry):
    if not isinstance(entry, dict):
        return None
    counter = entry.get('counter')
    fingerprint = entry.get('fingerprint')
    if not isinstance(counter, str) or not counter:
        return None
    if fingerprint is not None and not isinstance(fingerprint, str):
        fingerprint = None
    return {
        'counter': counter,
        'fingerprint': fingerprint,
    }


IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
GENERATED_MARKER = 'gallery_generated: true'


def camera_entry(tags):
    entry = {}
    for source, target in [('Model', 'model'), ('LensModel', 'lens'), ('ISO', 'iso')]:
        if tags.get(source):
            entry[target] = tags[source]
    if tags.get('FocalLength') is not None:
        entry['focal'] = round(float(tags['FocalLength']))
    if tags.get('FNumber') is not None:
        entry['aperture'] = round(float(tags['FNumber']), 1)
    if tags.get('ExposureTime') is not None:
        entry['shutter'] = format_shutter(float(tags['ExposureTime']))
    return entry


def photo_date(value):
    if not value:
        return ''
    for pattern in ('%Y:%m:%d %H:%M:%S', '%Y-%m-%d', '%Y-%m-%dT%H:%M:%S'):
        try:
            return datetime.strptime(value, pattern).isoformat()
        except ValueError:
            pass
    raise ValueError(f'Invalid photo date {value!r}; use YYYY-MM-DD.')


def build_gallery(root=REPO_ROOT):
    root = Path(root)
    source = root / 'photo_gallery'
    data_dir = root / '_data'
    thumbnails = root / 'assets/images/wildlife'
    pages = root / '_pages/wildlife'
    existing = {}
    for name, raw in load_json(data_dir / 'gallery_like_meta.json').items():
        meta = normalize_like_meta_entry(raw)
        if meta:
            existing[name] = meta

    records = []
    definitions = {}
    for folder in sorted(source.iterdir()):
        if folder.name.startswith('.'):
            continue
        if folder.is_file():
            if folder.suffix.lower() in IMAGE_EXTENSIONS:
                raise ValueError(f'Move {folder.name} into a species folder first.')
            continue
        slug = folder.name
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
            raise ValueError(f'Use a lowercase, hyphenated species folder: {slug}')
        definition = load_json(folder / 'species.json')
        if not isinstance(definition, dict):
            raise ValueError(f'{folder}/species.json must contain an object.')
        name = definition.get('name', slug.replace('-', ' ').title())
        definition = {
            'name': name,
            'category': definition.get('category', 'Other Wildlife'),
            'group': definition.get('group', ''),
            'scientific_name': definition.get('scientific_name', ''),
            'description': definition.get('description', ''),
            'references': definition.get('references', []),
            'cover': definition.get('cover', ''),
            'photos': definition.get('photos', {}),
        }
        definitions[slug] = definition
        for path in sorted(folder.rglob('*')):
            if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue
            relative = path.relative_to(source).as_posix()
            in_album = path.relative_to(folder).as_posix()
            records.append({
                'key': relative, 'path': path, 'slug': slug,
                'filename': in_album, 'fingerprint': fingerprint_file(path),
                'previous': existing.get(relative),
            })

    # Match moved/renamed files by content before allocating any new counters.
    matched = {record['key'] for record in records if record['previous']}
    old_by_fingerprint = {}
    for key, meta in existing.items():
        if key not in matched and meta.get('fingerprint'):
            old_by_fingerprint.setdefault(meta['fingerprint'], []).append(meta)
    reserved_counters = {meta['counter'] for meta in existing.values()}
    exif_result, like_result, albums = {}, {}, {}
    expected_thumbnails = set()
    for record in records:
        key, path, slug = record['key'], record['path'], record['slug']
        previous = record['previous']
        candidates = old_by_fingerprint.get(record['fingerprint'], [])
        if previous is None and candidates:
            previous = candidates.pop(0)
        counter = previous['counter'] if previous else slugify_counter_name(key)
        if not previous:
            if counter in reserved_counters:
                counter += '-' + hashlib.sha1(key.encode()).hexdigest()[:12]
            reserved_counters.add(counter)
        like_result[key] = {'counter': counter, 'fingerprint': record['fingerprint']}

        definition = definitions[slug]
        overrides = definition['photos'].get(record['filename'], {})
        try:
            tags = extract_exif(path) or {}
        except (ValueError, IndexError, struct.error):
            tags = {}
        camera = camera_entry(tags)
        if camera:
            exif_result[key] = camera
        if overrides.get('date'):
            date = photo_date(overrides['date'])
        else:
            try:
                date = photo_date(tags.get('DateTimeOriginal'))
            except ValueError:
                date = ''
        legacy_parts = path.stem.split(' -- ', 1)
        location = overrides.get('location', legacy_parts[1] if len(legacy_parts) > 1 else '')
        thumb = thumbnails / slug / (record['fingerprint'] + '.webp')
        expected_thumbnails.add(thumb)
        with Image.open(path) as image:
            width, height = image.size
            if image.getexif().get(0x0112) in {5, 6, 7, 8}:
                width, height = height, width
            if not thumb.exists():
                thumb.parent.mkdir(parents=True, exist_ok=True)
                preview = ImageOps.exif_transpose(image).convert('RGB')
                preview.thumbnail((960, 960))
                preview.save(thumb, 'WEBP', quality=82, method=4)
        photo = {
            'filename': record['filename'],
            'path': '/' + path.relative_to(root).as_posix(),
            'thumbnail': '/' + thumb.relative_to(root).as_posix(),
            'width': width, 'height': height,
            'caption': overrides.get('caption', definition['name']),
            'location': location, 'date': date,
            'featured': bool(overrides.get('featured', False)),
            'camera': camera, 'counter': counter,
        }
        if slug not in albums:
            albums[slug] = {field: definition[field] for field in (
                'name', 'category', 'group', 'scientific_name', 'description', 'references')}
            albums[slug].update({'slug': slug, 'url': f'/wildlife-gallery/{slug}/', 'photos': []})
        albums[slug]['photos'].append(photo)

    for slug, album in albums.items():
        album['photos'].sort(key=lambda photo: photo['filename'].casefold())
        album['photos'].sort(key=lambda photo: photo['date'], reverse=True)
        album['photos'].sort(key=lambda photo: photo['featured'], reverse=True)
        configured_cover = definitions[slug]['cover']
        if configured_cover and not any(photo['filename'] == configured_cover for photo in album['photos']):
            raise ValueError(f'Cover {configured_cover!r} not found in {slug}.')
        album['cover'] = next((photo for photo in album['photos']
                               if photo['filename'] == configured_cover), album['photos'][0])
        album['count'] = len(album['photos'])
        album['locations'] = sorted({photo['location'] for photo in album['photos'] if photo['location']})

    data_dir.mkdir(parents=True, exist_ok=True)
    pages.mkdir(parents=True, exist_ok=True)
    index = [{key: value for key, value in album.items() if key != 'photos'}
             for album in sorted(albums.values(), key=lambda album: album['name'].casefold())]
    for filename, result in [('gallery_exif.json', exif_result),
                             ('gallery_like_meta.json', like_result),
                             ('gallery_index.json', index),
                             ('gallery_albums.json', albums)]:
        save_json(data_dir / filename, result)
    for slug, album in albums.items():
        title = json.dumps(album['name'], ensure_ascii=False)
        (pages / f'{slug}.html').write_text(
            f'---\nlayout: wildlife-album\ntitle: {title}\n'
            f'permalink: {album["url"]}\ngallery_species: {slug}\n'
            f'{GENERATED_MARKER}\n---\n', encoding='utf-8')
    for page in pages.glob('*.html'):
        if page.stem not in albums and GENERATED_MARKER in page.read_text():
            page.unlink()
    for thumb in thumbnails.rglob('*.webp'):
        if thumb not in expected_thumbnails:
            thumb.unlink()
    print(f'Updated {len(records)} photographs across {len(albums)} albums.')
    return albums


if __name__ == '__main__':
    build_gallery()
