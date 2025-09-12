# Haowen Zhou's Academic Homepage

**Live Website**: [https://hwzhou2020.github.io/](https://hwzhou2020.github.io/)

This is the personal academic homepage of Haowen Zhou, a PhD candidate in Electrical Engineering at Caltech, advised by Prof. Changhuei Yang. The website showcases research in computational microscopy, neural fields, AI, digital pathology, and 3D imaging.

## Website Features

### 🎨 **Modern Design & Styling**
- **Typography**: Clean, readable fonts with improved line spacing
- **Color Scheme**: Professional academic color palette with orange accents
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Contemporary Layout**: Card-based publication display with hover effects

### 📰 **Smart News Section**
- **Auto-Management**: Automatically shows the 5 most recent news items
- **Expandable**: "Show More News" button to reveal complete news history
- **Easy Updates**: Simply add new news items at the top - no manual configuration needed

### 📚 **Enhanced Publications**
- **Selected Publications**: Curated list on homepage with rectangular image layout
- **Full Publications**: Complete list on dedicated publications page with grid layout
- **Interactive Elements**: Hover effects and smooth transitions
- **Mobile Optimized**: Responsive image sizing and layout

### 🔗 **Professional Links**
- **Social Profiles**: LinkedIn, ORCID, Google Scholar integration
- **Research Links**: GitHub, project pages, and data repositories
- **Contact Information**: Email and institutional affiliation

## Technical Details

### **Built With**
- **Jekyll**: Static site generator
- **GitHub Pages**: Hosting platform
- **Minimal Mistakes Theme**: Base template (heavily customized)
- **Custom CSS/JavaScript**: Enhanced styling and functionality

### **Key Improvements Made**
1. **Typography & Readability**: Modern font stack and improved spacing
2. **Color Scheme**: Professional academic color palette
3. **Publication Layout**: Card-based design with variable image sizing
4. **Mobile Optimization**: Responsive design for all screen sizes
5. **Accessibility**: Focus indicators and screen reader support
6. **Loading Optimization**: Lazy loading for images
7. **News Management**: Automatic top-5 display with expand functionality
8. **HTML Conversion**: Converted homepage from Markdown to HTML for better JavaScript compatibility
9. **SEO Optimization**: Comprehensive meta tags for search engine visibility

## Local Development

To run this website locally:

1. **Prerequisites**: Install Ruby, Bundler, and Node.js
2. **Clone**: `git clone https://github.com/hwzhou2020/hwzhou2020.github.io.git`
3. **Install**: `bundle install`
4. **Serve**: `bundle exec jekyll serve`
5. **View**: Open `http://localhost:4000`

## Content Management

### **Adding News**
Simply add new news items at the top of the news section in `_pages/about.html`:
```html
<div class="news-item">
  <span class="news-date">MM/DD/YYYY</span> - Your news content here
</div>
```

### **Adding Publications**
Add publications to `_pages/publications.md` using the established format with images and metadata.

### **Updating Profile**
Modify `_config.yml` for basic information, social links, and site configuration.

### **Homepage Structure**
- **Main Content**: `_pages/about.html` (converted from Markdown for better JavaScript compatibility)
- **News Management**: Automatic top-5 display with expand/collapse functionality
- **Publication Display**: Card-based layout with rectangular images at bottom

## Research Focus

- **Computational Microscopy**: Empowering imaging techniques with algorithms
- **Neural Fields**: Physics-based neural representations for microscopy
- **AI in Healthcare**: Digital pathology and medical imaging
- **3D Imaging**: Volumetric reconstruction and analysis
- **Fourier Ptychographic Microscopy**: High-resolution, large field-of-view imaging

## Contact

- **Email**: hzhou7@caltech.edu
- **Institution**: California Institute of Technology
- **Department**: Electrical Engineering
- **Lab**: [Biophotonics Lab](https://biophot.caltech.edu/)

---

*This website is built using the Minimal Mistakes Jekyll theme, customized for academic use with modern styling and enhanced functionality.*