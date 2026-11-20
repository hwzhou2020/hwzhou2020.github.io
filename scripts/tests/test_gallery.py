import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from PIL import Image, TiffImagePlugin


SCRIPT = Path(__file__).resolve().parents[1] / 'extract_gallery_exif.py'
spec = importlib.util.spec_from_file_location('gallery', SCRIPT)
gallery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gallery)


class GalleryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'photo_gallery').mkdir()
        (self.root / '_data').mkdir()

    def species(self, slug, **metadata):
        folder = self.root / 'photo_gallery' / slug
        folder.mkdir(exist_ok=True)
        (folder / 'species.json').write_text(json.dumps(metadata))
        return folder

    def image(self, folder, name='DSC001.jpg', color='red'):
        path = folder / name
        Image.new('RGB', (30, 20), color).save(path)
        return path

    def test_migration_and_rename_preserve_counter_and_original(self):
        folder = self.species('owl', name='Owl', category='Birds')
        path = self.image(folder)
        fingerprint = gallery.fingerprint_file(path)
        gallery.save_json(self.root / '_data/gallery_like_meta.json', {
            'old-name.jpg': {'counter': 'existing-public-id', 'fingerprint': fingerprint}})
        albums = gallery.build_gallery(self.root)
        self.assertEqual(albums['owl']['photos'][0]['counter'], 'existing-public-id')
        self.assertEqual(gallery.fingerprint_file(path), fingerprint)
        path.rename(folder / 'new-name.jpg')
        albums = gallery.build_gallery(self.root)
        self.assertEqual(albums['owl']['photos'][0]['counter'], 'existing-public-id')

    def test_identical_filenames_in_different_species_have_distinct_counters(self):
        self.image(self.species('owl'), color='red')
        self.image(self.species('fox'), color='blue')
        albums = gallery.build_gallery(self.root)
        counters = {album['photos'][0]['counter'] for album in albums.values()}
        self.assertEqual(len(counters), 2)

    def test_dates_featured_cover_location_and_arbitrary_filenames(self):
        folder = self.species('owl', name='Great Horned Owl', cover='DSC002.jpg', photos={
            'DSC001.jpg': {'date': '2026-01-01', 'featured': True, 'location': 'Park'},
            'DSC002.jpg': {'date': '2026-02-01'},
        })
        self.image(folder, 'DSC001.jpg')
        self.image(folder, 'DSC002.jpg', 'blue')
        album = gallery.build_gallery(self.root)['owl']
        self.assertEqual(album['photos'][0]['filename'], 'DSC001.jpg')
        self.assertEqual(album['photos'][0]['caption'], 'Great Horned Owl')
        self.assertEqual(album['cover']['filename'], 'DSC002.jpg')
        self.assertEqual(album['locations'], ['Park'])

    def test_rerun_is_idempotent(self):
        self.image(self.species('owl'))
        gallery.build_gallery(self.root)
        before = {p.name: p.read_bytes() for p in (self.root / '_data').glob('*.json')}
        gallery.build_gallery(self.root)
        after = {p.name: p.read_bytes() for p in (self.root / '_data').glob('*.json')}
        self.assertEqual(before, after)

    def test_location_hierarchy_preserves_regions_and_unknown_places(self):
        gallery.save_json(self.root / '_data/gallery_places.json', {
            'Maui, Hawaii': {'country': 'United States', 'state': 'Hawaii'},
            'Madison, Wisconsin': {'country': 'United States', 'state': 'Wisconsin'},
        })
        folder = self.species('bird', photos={
            'a.jpg': {'location': 'Maui, Hawaii'},
            'b.jpg': {'location': 'Madison, Wisconsin'},
            'c.jpg': {'location': 'Unmapped place'},
        })
        for name in ['a.jpg', 'b.jpg', 'c.jpg']:
            self.image(folder, name)
        album = gallery.build_gallery(self.root)['bird']
        self.assertEqual(album['location_details'], [
            {'name': 'Madison, Wisconsin', 'country': 'United States', 'state': 'Wisconsin'},
            {'name': 'Maui, Hawaii', 'country': 'United States', 'state': 'Hawaii'},
            {'name': 'Unmapped place', 'country': '', 'state': ''},
        ])
        index = gallery.load_json(self.root / '_data/gallery_index.json')
        self.assertEqual(index[0]['location_details'], album['location_details'])

    def test_camera_capture_date_and_orientation_survive_import(self):
        for extension in ['jpg', 'webp']:
            with self.subTest(extension=extension):
                folder = self.species('owl-' + extension, name='Owl')
                exif = Image.Exif()
                exif[0x0110] = 'Test Camera'
                exif[0x0112] = 6
                exif[0x8769] = {
                    0xA434: 'Test Lens', 0x920A: TiffImagePlugin.IFDRational(600),
                    0x829D: TiffImagePlugin.IFDRational(63, 10),
                    0x829A: TiffImagePlugin.IFDRational(1, 1000),
                    0x8827: 100, 0x9003: '2026:11:14 12:34:56',
                }
                path = folder / ('camera.' + extension)
                Image.new('RGB', (30, 20)).save(path, exif=exif)
                original = path.read_bytes()
                photo = gallery.build_gallery(self.root)['owl-' + extension]['photos'][0]
                self.assertEqual(photo['camera'], {
                    'model': 'Test Camera', 'lens': 'Test Lens', 'focal': 600,
                    'aperture': 6.3, 'shutter': '1/1000', 'iso': 100,
                })
                self.assertEqual(photo['date'], '2026-11-14T12:34:56')
                self.assertEqual((photo['width'], photo['height']), (20, 30))
                self.assertEqual(path.read_bytes(), original)

    def test_150_photos_in_one_album(self):
        folder = self.species('owl', name='Owl')
        source = self.image(folder, '000.jpg')
        for index in range(1, 150):
            shutil.copyfile(source, folder / f'{index:03}.jpg')
        album = gallery.build_gallery(self.root)['owl']
        self.assertEqual(album['count'], 150)
        self.assertEqual(len({photo['counter'] for photo in album['photos']}), 150)
        self.assertTrue((self.root / '_pages/wildlife/owl.html').exists())

    def test_removed_album_cleans_only_generated_pages(self):
        folder = self.species('owl')
        photo = self.image(folder)
        gallery.build_gallery(self.root)
        custom_page = self.root / '_pages/wildlife/manual.html'
        custom_page.write_text('User-authored page')
        photo.unlink()
        gallery.build_gallery(self.root)
        self.assertFalse((self.root / '_pages/wildlife/owl.html').exists())
        self.assertEqual(custom_page.read_text(), 'User-authored page')
        self.assertFalse(list((self.root / 'assets/images/wildlife').rglob('*.webp')))

    def test_invalid_cover_is_reported(self):
        folder = self.species('owl', cover='missing.jpg')
        self.image(folder)
        with self.assertRaisesRegex(ValueError, 'Cover.*not found'):
            gallery.build_gallery(self.root)


if __name__ == '__main__':
    unittest.main()
