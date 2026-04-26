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

### Photo gallery likes
The photo gallery in `_pages/beyond-research.html` uses two layers for heart counts:
- `_data/gallery_like_seeds.json` stores one-time initial like counts for each photo. New photos get a random seed from 1 to 100 when you run `python3 scripts/extract_gallery_exif.py`.
- CounterAPI V1 public counters track additional heart clicks across visitors after publish.

This works on a static GitHub Pages site without a custom backend, but the live counters are public and subject to the provider's per-path rate limits.


## Contact
- **Email**: hzhou7@caltech.edu
- **Institution**: California Institute of Technology
- **Department**: Electrical Engineering
- **Lab**: [Biophotonics Lab](https://biophot.caltech.edu/)

---

Built with the Minimal Mistakes Jekyll theme and tailored for academic portfolios with modern styling, automated news curation, and publication-focused layouts.
