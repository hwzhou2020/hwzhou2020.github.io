#!/usr/bin/env python3
"""
Extract EXIF metadata from photo_gallery/ and write _data/gallery_exif.json.
Also maintain _data/gallery_like_seeds.json with one-time random initial like
counts for new photos.
Run this whenever you add new photos:  python3 scripts/extract_gallery_exif.py
"""
import json
import os
import random
import struct

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO_DIR = os.path.join(REPO_ROOT, 'photo_gallery')
OUT_PATH  = os.path.join(REPO_ROOT, '_data', 'gallery_exif.json')
SEED_PATH = os.path.join(REPO_ROOT, '_data', 'gallery_like_seeds.json')


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
}


def extract_exif(path):
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
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    exif_result = {}
    existing_seeds = load_json(SEED_PATH)
    seed_result = {}
    photo_files = sorted(
        fname for fname in os.listdir(PHOTO_DIR)
        if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))
    )

    for fname in photo_files:
        if fname in existing_seeds:
            seed_result[fname] = existing_seeds[fname]
        else:
            seed_result[fname] = random.randint(1, 100)
            print(f'  seed: {fname} -> {seed_result[fname]}')

        if not fname.lower().endswith(('.jpg', '.jpeg')):
            continue
        tags = extract_exif(os.path.join(PHOTO_DIR, fname))
        if not tags:
            print(f'  skip (no EXIF): {fname}')
            continue
        entry = {}
        if tags.get('Model'):     entry['model']    = tags['Model']
        if tags.get('LensModel'): entry['lens']     = tags['LensModel']
        fl = tags.get('FocalLength')
        if fl is not None:        entry['focal']    = round(fl)
        fn = tags.get('FNumber')
        if fn is not None:        entry['aperture'] = round(fn * 10) / 10
        et = tags.get('ExposureTime')
        if et is not None:        entry['shutter']  = format_shutter(et)
        iso = tags.get('ISO')
        if iso is not None:       entry['iso']      = iso
        exif_result[fname] = entry
        print(f'  ok: {fname}')

    save_json(OUT_PATH, exif_result)
    save_json(SEED_PATH, seed_result)
    print(f'\nWrote {len(exif_result)} EXIF entries → {OUT_PATH}')
    print(f'Wrote {len(seed_result)} like seeds → {SEED_PATH}')


if __name__ == '__main__':
    main()
