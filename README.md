# Haowen Zhou's Academic Homepage

**Live Website**: [https://hwzhou2020.github.io/](https://hwzhou2020.github.io/)

Personal academic site for Haowen Zhou, PhD candidate in Electrical Engineering at Caltech (Biophotonics Lab, Prof. Changhuei Yang). 

## Content Management

### Adding news
Add new entries at the top of `_pages/about.html`:

```html
<div class="news-item">
  <span class="news-date">MM/DD/YYYY</span> - Your news content here
</div>
```

### Adding publications
Use the existing publication blocks in `_pages/publications.md` (image, title, venue, links). The homepage automatically highlights the "selected" subset defined near the top of that file.

### Updating profile information
Edit `_config.yml` to change name, tagline, email, social links, and SEO metadata. Additional navigation labels live in `_data/navigation.yml`.

### Homepage structure
- `_pages/about.html`: main content and news timeline (converted from Markdown to HTML for JavaScript-driven behavior)
- `_pages/publications.md`: detailed publication grid
- `_sass` and `assets/css`: house style overrides and animations

### Adding wildlife photos

The Wildlife Gallery shows one card per species, with separate albums, animal and bird-group filters, species search, and camera details. Albums show 24 photos at a time; thumbnails load separately from full-size originals. Beyond Research keeps its activities and links to the gallery.

Search and filters appear first, followed by selected albums from the `gallery_highlights` list in `_pages/wildlife-gallery.html`, in that list's order. The complete alphabetical collection follows, including the highlighted albums. Search, filters, counts, and “Show more” apply to the complete collection. Highlights hide while a search or filter is active and return when the controls are cleared.

Photos live in species folders. Existing filenames have been preserved, and new filenames can be anything unique within their folder:

```text
photo_gallery/
  great-horned-owl/
    species.json
    Great Horned Owl.jpg
    Juvenile Great Horned Owl.jpg
    2026-11-14-001.jpg
```

To add photos to an existing species, copy them into its folder and run:

```sh
python3 scripts/extract_gallery_exif.py
```

Then preview, commit, and publish the updated photos, metadata, generated album pages, and thumbnails together. Keep EXIF metadata when exporting photographs to retain the camera, lens, focal length, aperture, shutter speed, ISO, and capture date. The script leaves originals untouched. If Pillow is missing, install it with `python3 -m pip install -r scripts/requirements-gallery.txt`.

To add a new species, create a lowercase, hyphenated folder and a `species.json` file:

```json
{
  "name": "Great Horned Owl",
  "category": "Birds",
  "group": "Raptors & Owls",
  "cover": "2026-11-14-001.jpg"
}
```

Add images and run the same command. The album page is generated automatically. Categories currently include `Birds`, `Mammals`, `Reptiles`, and `Insects`; new categories appear automatically when used. Bird groups are visitor-friendly browsing labels, not formal taxonomic ranks. If a folder has no `species.json`, its name supplies the album title and it appears under `Other Wildlife` until classified.

Album introductions (`description`) and their reference links appear after the photographs.

Each album has an explicitly selected `cover` filename in `species.json`. Adding new photos keeps that cover in place; edit `cover` and rerun the importer to choose another. Animal-group and bird-group dropdown counts show the total number of albums in each group.

Optional species fields are `scientific_name` and `description`. Leave a scientific name blank when identification is uncertain. Set `cover` to an existing filename, or omit it to use the first photo. Optional per-photo information goes in the same file:

```json
{
  "name": "Great Horned Owl",
  "category": "Birds",
  "group": "Raptors & Owls",
  "photos": {
    "2026-11-14-001.jpg": {
      "caption": "A juvenile in the evening light",
      "location": "Park name, California",
      "date": "2026-11-14",
      "featured": true
    }
  }
}
```

Featured photos appear first, followed by capture date (newest first), then filename for undated photos. Captions default to the species name. Locations are optional and appear alongside individual photos when supplied. The gallery filters by species name, animal group, bird group, country, state/region, and location. Country and state selections narrow the available places; each option counts matching albums once. Location filters show albums containing at least one photo from the selected area. Opening an album still shows its complete photo collection. Files may also be nested in outing subfolders within a species folder; use relative paths such as `2026-11-14/DSC001.jpg` in `cover` and `photos`.

Some locations were inferred by matching capture timestamps, camera models, and retained camera filenames to RAW files in the external `Wildlife photos` archive. Their `location_source` records preserve the matching method and outing folder; these are broad locations, not GPS fixes. Folders naming multiple sites use a shared region. Existing photographer-confirmed locations take precedence. Unresolved photos are grouped by date in `scripts/wildlife-location-review.json`, which is excluded from the built site. Adding photos does not automatically search the external drive. The country and state for each location are defined once in `_data/gallery_places.json`; add an entry there when introducing a new location. An unmapped place remains available in the location selector but is not guessed into a country or state.

Edit source images and `species.json`, then rerun the script. `_data/gallery_albums.json`, `_data/gallery_index.json`, `_data/gallery_exif.json`, `_data/gallery_like_meta.json`, `_pages/wildlife/`, and `assets/images/wildlife/` are generated outputs. Avoid editing them by hand. Run importer checks with `python3 -m unittest discover -s scripts/tests` and interaction checks with `node --test scripts/tests/test_wildlife_gallery.cjs`.

### Photo gallery likes
Each species album uses three layers for heart counts:
- `_data/gallery_like_meta.json` stores a stable public counter key for each photo, indexed by its path relative to `photo_gallery/`. The importer preserves existing keys across reruns and carries them forward if you move or rename a photo without changing the underlying image file. Different species can use the same filename.
- CounterAPI V1 public counters track heart clicks across visitors after publish.
- Browser `localStorage` caches the last known displayed total and any unsynced clicks so a page refresh does not appear to reset likes if the remote counter read/write is delayed or fails.

This works on a static GitHub Pages site without a custom backend, but the live counters are public and subject to the provider's per-path rate limits.


---

Built with the Minimal Mistakes Jekyll theme and tailored for academic portfolios with modern styling, automated news curation, and publication-focused layouts.
