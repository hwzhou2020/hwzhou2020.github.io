---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<html>
  <head>
    <link href='https://fonts.googleapis.com/css?family=Noto Sans' rel='stylesheet'>
    <style>
      /* Typography & Readability Improvements */
      body {
        font-family: 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: #2d3748;
      }

      h1, h2, h3, h4, h5, h6 {
        font-weight: 600;
        line-height: 1.3;
        margin-bottom: 0.5em;
        color: #1a365d;
      }

      p {
        margin-bottom: 1em;
        line-height: 1.7;
      }

      a {
        color: #EC8F5E;
        text-decoration: none;
        transition: color 0.3s ease;
      }

      a:hover {
        color: #B2533E;
        text-decoration: underline;
      }

      /* Publication Layout Improvements */
      .publication {
        display: grid;
        grid-template-columns: 150px 1fr;
        align-items: flex-start;
        gap: 20px;
        margin-bottom: 30px;
        padding: 20px;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #EC8F5E;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
      }

      .publication:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      }

      .publication-image {
        width: 150px;
        height: 150px;
        overflow: hidden;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      }

      .publication-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.3s ease;
      }

      .publication-image img:hover {
        transform: scale(1.05);
      }

      .publication-details {
        flex-grow: 1;
      }

      .publication-title {
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 8px;
        color: #1a365d;
      }

      .publication-authors {
        font-size: 0.95em;
        color: #4a5568;
        margin-bottom: 6px;
      }

      .publication-venue {
        font-size: 0.9em;
        color: #B2533E;
        font-weight: 500;
        margin-bottom: 8px;
      }

      .publication-links {
        margin-bottom: 10px;
      }

      .publication-links a {
        display: inline-block;
        margin-right: 12px;
        padding: 4px 8px;
        background: #e2e8f0;
        border-radius: 4px;
        font-size: 0.85em;
        transition: background-color 0.2s ease;
      }

      .publication-links a:hover {
        background: #cbd5e0;
      }

      .publication-abstract {
        font-size: 0.9em;
        color: #718096;
        line-height: 1.6;
      }

      /* News Section Styling */
      .news-item {
        margin-bottom: 15px;
        padding: 12px;
        background: #f7fafc;
        border-left: 3px solid #186F65;
        border-radius: 4px;
      }

      .news-date {
        font-weight: 600;
        color: #2d3748;
      }

      /* Mobile Optimization */
      @media (max-width: 768px) {
        .publication {
          grid-template-columns: 1fr;
          gap: 15px;
          padding: 15px;
        }

        .publication-image {
          width: 100%;
          height: 200px;
          justify-self: center;
        }

        body {
          font-size: 16px;
        }

        .publication-title {
          font-size: 1.05em;
        }
      }

      /* Accessibility Improvements */
      .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
      }

      a:focus {
        outline: 2px solid #EC8F5E;
        outline-offset: 2px;
      }

      /* Loading Optimization */
      .publication-image img {
        loading: lazy;
      }

      /* Search and Sort Controls */
      .publications-controls {
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
        flex-wrap: wrap;
        align-items: center;
      }

      .search-box {
        position: relative;
        flex: 1;
        min-width: 250px;
      }

      .search-box input {
        width: 100%;
        padding: 10px 40px 10px 12px;
        border: 2px solid #e2e8f0;
        border-radius: 6px;
        font-size: 14px;
        transition: border-color 0.2s ease;
      }

      .search-box input:focus {
        outline: none;
        border-color: #EC8F5E;
        box-shadow: 0 0 0 3px rgba(236, 143, 94, 0.1);
      }

      .search-box button {
        position: absolute;
        right: 8px;
        top: 50%;
        transform: translateY(-50%);
        background: none;
        border: none;
        font-size: 18px;
        color: #a0aec0;
        cursor: pointer;
        padding: 4px;
        border-radius: 4px;
        transition: color 0.2s ease;
      }

      .search-box button:hover {
        color: #718096;
      }

      .sort-controls {
        display: flex;
        align-items: center;
        gap: 8px;
      }

      .sort-controls label {
        font-weight: 500;
        color: #4a5568;
      }

      .sort-controls select {
        padding: 8px 12px;
        border: 2px solid #e2e8f0;
        border-radius: 6px;
        font-size: 14px;
        background: white;
        cursor: pointer;
        transition: border-color 0.2s ease;
      }

      .sort-controls select:focus {
        outline: none;
        border-color: #EC8F5E;
        box-shadow: 0 0 0 3px rgba(236, 143, 94, 0.1);
      }

      .publications-note {
        font-size: 0.9em;
        color: #718096;
        margin-bottom: 20px;
        font-style: italic;
      }

      /* Mobile optimization for controls */
      @media (max-width: 768px) {
        .publications-controls {
          flex-direction: column;
          align-items: stretch;
        }

        .search-box {
          min-width: auto;
        }

        .sort-controls {
          justify-content: space-between;
        }
      }

      .clustermaps-widget{
        display: none;
      }
  </style>
  </head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-J4XRR1S1L4"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-J4XRR1S1L4');
  </script>
<body>

<div class="bio-section">
  <p>
    I am a PhD candidate in the Department of Electrical Engineering at Caltech, advised by 
    <a href="https://biophot.caltech.edu/">Prof. Changhuei Yang</a>.
    My current research interests include:
  </p>
  <ul>
    <li>Computational microscopy - empowering imaging techniques with algorithms</li>
    <li>Synergizing microscopy, computation and artificial intelligence to advance life science</li>
  </ul>
  <p>
    My aspiration is to become an engineer-scientist who advances scientific discovery through innovative engineering designs.
  </p>
  <p>
    <strong>I am currently on the 2025-2026 job market.</strong>
  </p>
</div>

<section class="news-section">
  <h2>News</h2>
  
  <div class="news-item">
    <span class="news-date">08/19/2025</span> - I presented my work on neural fields for computational microscopy at Optica Imaging Congress, Seattle.
  </div>
  
  <div class="news-item">
    <span class="news-date">07/29/2025</span> - I gave an invited talk at Rice University on "Physics-based computational microscopy to advance life science research".
  </div>
  
  <div class="news-item">
    <span class="news-date">06/04/2025</span> - I delivered an invited talk in ESE Seminar Series at Washington University in St. Louis, titled "Empowering microscopes with physics-based computation" 
    <a href="https://happenings.wustl.edu/event/ese-seminar-series-haowen-zhou">[Talk page]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">04/30/2025</span> - I delivered an invited talk in Computer Vision Seminar Series at University of Maryland, College Park, titled "Synergizing microscopy and computation to advance life science research"
  </div>
  
  <div class="news-item">
    <span class="news-date">02/25/2025</span> - Check out our new paper "Single-shot volumetric fluorescence imaging with neural fields" on Advanced Photonics 
    <a href="https://doi.org/10.1117/1.AP.7.2.026001">[paper link]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">12/03/2024</span> - I am awarded Schmidt Academy for Software Engineering Graduate Research Fellowship. The support will start on Jan. 2025 for contributions to the algorithm and software development towards computational microscopy, specifically Fourier Ptychographic Microscopy. 
    <a href="https://sase.caltech.edu/people/gra-fellows.html">[Schmidt Academy GRA Fellows]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">08/06/2024</span> - Our new paper titled "Investigating 3D microbial community dynamics of the rhizosphere using quantitative phase and fluorescence microscopy" is online at 
    <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2403122121">PNAS</a>. 
    <a href="https://www.science.org/doi/10.1126/science.adt0513">[Science.org News]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">05/24/2024</span> - I am awarded <strong>SPIE Optics and Photonics Scholarship</strong>. 
    <a href="https://spie.org/membership/student-hub/scholarships/optics-and-photonics-education-scholarships/current-winners#_=_">[Webpage]</a> 
    <a href="/files/Haowen Zhou PR24.pdf">[PDF]</a>
    <a href="https://www.ee.caltech.edu/news/haowen-zhou-awarded-spie-optics-and-photonics-scholarship">[News]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">03/06/2024</span> - The new paper "AI-guided histopathology predicts brain metastasis in lung cancer patients" has been featured on the Caltech homepage. 
    <a href="https://www.caltech.edu/about/news/using-ai-to-predict-the-spread-of-lung-cancer/">[News]</a>
  </div>
  
  <div class="news-item">
    <span class="news-date">03/04/2024</span> - My new paper on "AI-guided histopathology predicts brain metastasis in lung cancer patients" is online today. Check my publication list 
    <a href="https://hwzhou2020.github.io/publications/">here</a>!
  </div>
  
  <div class="news-item">
    <span class="news-date">02/14/2024</span> - I passed my candidacy exam!
  </div>
  
  <div class="news-item">
    <span class="news-date">11/21/2023</span> - My personal homepage is online!
  </div>
  
  <div class="news-item">
    <span class="news-date">06/30/2021</span> - I joined Caltech Biophotonics Lab!
  </div>
</section>

<section class="publications-section">
  <h2>Selected Publications</h2>
  
  <div class="publications-controls">
    <div class="search-box">
      <input type="text" id="publicationSearch" placeholder="Search publications..." aria-label="Search publications">
      <button type="button" id="clearSearch" aria-label="Clear search">×</button>
    </div>
    
    <div class="sort-controls">
      <label for="sortBy">Sort by:</label>
      <select id="sortBy" aria-label="Sort publications">
        <option value="date">Date (Newest First)</option>
        <option value="date-old">Date (Oldest First)</option>
        <option value="title">Title (A-Z)</option>
        <option value="venue">Venue</option>
      </select>
    </div>
  </div>
  
  <p class="publications-note">
    Full publication list <a href="https://hwzhou2020.github.io/publications/">here</a>. 
    Clicking paper titles will direct to the preprint or paper page.
  </p>
  
  <div id="publicationsContainer">


<!-- pub 19 -->
<div class="publication" data-year="2025" data-venue="arXiv" data-title="Digital defocus aberration interference for automated optical microscopy">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/DAbI_cover.png" alt="DAbI cover image" loading="lazy">
  </div>
  <div class="publication-details">
    <div class="publication-title">
      <a href="https://arxiv.org/abs/2507.10867">Digital defocus aberration interference for automated optical microscopy</a>
    </div>
    <div class="publication-authors">
      <strong>Haowen Zhou*</strong>, Shi Zhao*, Yujie Fan, Zhenyu Dong, Oumeng Zhang, Viviana Gradinaru, Changhuei Yang
    </div>
    <div class="publication-venue">arXiv, 2025</div>
    <div class="publication-links">
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/DAbI.txt">BibTex</a>
      <a href="https://hwzhou2020.github.io/DAbI-Web/">Project Page & Code</a>
      <a href="https://osf.io/dvztc/">Data</a>
    </div>
    <div class="publication-abstract">
      We recently discovered a phenomenon that the digitally summed Fourier spectrum of two images acquired from two-angle illumination exhibits interference-like fringe modulation when the sample is out-of-focus.
      These digital fringes correlate directly with defocus through a physics-based relation. Based on this principle, we developed an automatic, efficient, and generalizable defocus detection method termed digital defocus aberration interference (DAbI).
    </div>
  </div>
</div>

<br>
<br>
<br>

<!-- pub 18 -->
<div class="publication">
  <div class="publication-details">
    <font size="4">
      <a href="https://arxiv.org/abs/2504.16247" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            Analytic Fourier ptychotomography for volumetric refractive index imaging
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Zhenyu Dong*, <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Ruizhi Cao*, Oumeng Zhang, Shi Zhao, Panlang Lyu, Reinaldo E Alcalde, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
      <span style="color: #B2533E;">arXiv, 2025</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/AFP.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
      <a href="https://mrdongzhenyu.github.io/AFP-Web/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #186F65;">[Project Page & Code]</span>
      </a>
      <a href="https://osf.io/f7tqa/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #FCE09B;">{Data}</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We propose Fourier Ptychotomography (AFP), a new computational microscopy technique that analytically reconstructs aberration-free, complex-valued 3D RI distributions without iterative optimization or axial scanning. AFP incorporates a new concept named finite sample thickness (FST) prior, thereby simplifying the inverse scattering problem into solving linear equations. 
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/AFP_cover.png">

<br>
<br>
<br>

<!-- pub 17 -->
<div class="publication">
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1117/1.AP.7.2.026001" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            Single-shot volumetric fluorescence imaging with neural fields
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Oumeng Zhang*, <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Brandon Y Feng, Elin M Larsson, Reinaldo E Alcalde, Siyuan Yin, Catherine Deng, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
      <span style="color: #B2533E;">Advanced Photonics, 2025</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/SVF.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
      <a href="https://hwzhou2020.github.io/SVF-Web/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #186F65;">[Project Page & Code]</span>
      </a>
      <a href="https://osf.io/4a5ws/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #FCE09B;">{Data}</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Single-shot volumetric fluorescence (SVF) imaging captures biological processes with high temporal resolution and a large field of view, unlike traditional methods requiring multiple axial plane scans. Existing SVF methods often face limitations due to large, complex point spread functions (PSFs), affecting signal-to-noise ratio, resolution, and field of view. The paper introduces a QuadraPol PSF combined with neural fields, using a compact custom polarizer and a polarization camera to detect fluorescence and encode the 3D scene within a compact PSF without depth ambiguity. 
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/SVF_cover.jpg">

<br>
<br>
<br>

<div class="publication">
  <div class="publication-details">
    <font size="4">
      <a href=" https://doi.org/10.1002/path.6263" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            AI-guided histopathology predicts brain metastasis in lung cancer patients
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Mark Watson*, Cory T. Bernadt, Steven (Siyu) Lin, Chieh-yu Lin, Jon H. Ritter, Alexander Wein, Simon Mahler, Sid Rawal, Ramaswamy Govindan, Changhuei Yang, Richard J. Cote
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Journal of Pathology, 2024</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/AI_NSCLC.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
      <a href="https://github.com/hwzhou2020/NSCLC_ResNet" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #186F65;">[Code]</span>
      </a>
      <a href="https://doi.org/10.22002/dw66e-mbs82" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #FCE09B;">{Data}</span>
      </a>
      <a href="https://www.caltech.edu/about/news/using-ai-to-predict-the-spread-of-lung-cancer/" style="text-decoration: none;">
      &nbsp; &nbsp;
      <strong>
        <span style="color: #B2533E;">News</span>
      </strong>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Brain metastases can occur in nearly half of patients with early and locally advanced (stage I–III) non-small cell lung cancer (NSCLC). There are no reliable histopathologic or molecular means to identify those who are likely to develop brain metastases. We sought to determine if deep learning could be applied to routine H&E-stained primary tumor tissue sections from stage I–III NSCLC patients to predict the development of brain metastasis.
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/Jpath-cover.jpg">

<br>
<br>
<br>

<!-- pub 11 -->
<div class="publication">
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1364/OPTICA.505283" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            FPM-INR: Fourier ptychographic microscopy image stack reconstruction using implicit neural representations
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Brandon Y. Feng*, Haiyun Guo, Siyu Lin, Mingshu Liang, Christopher A. Metzler, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
      <span style="color: #B2533E;">Optica, 2023</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/FPM-INR.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
      <a href="https://hwzhou2020.github.io/FPM-INR-Web/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #186F65;">[Project Page & Code]</span>
      </a>
      <a href="https://doi.org/10.22002/7aer7-qhf77" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #FCE09B;">{Data}</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Fourier ptychographic microscope images the biological samples with high-resolution and large field-of-view simultaneously. However, this microscope faces challenges with long image stack reconstruction time and huge data volumes. We designed physics-based neural signal representations to tackle these challenges and showed potential in facilitating remote diagnosis, digital pathology, and efficient clinical data packaging.
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/FPM-INR-Cover.jpg">

<br>
<br>
<br>

<!-- <font size="5">
  <strong>
    Teaching
  </strong>
</font>
<br>
<font size="3">
  Caltech EE151 - Electromagnetic Engineering (Head TA for Spring 2024)
  <br>
</font>
<font size="3">
  <p style="margin-left: 25px;">
    <span style="color: gray;">
      Foundations of circuit theory-electric fields, magnetic fields, transmission lines, and Maxwell's equations, with engineering applications.
    </span>
  </p>
</font>

<!-- <font size="3">
  Caltech EE151 - Electromagnetic Engineering (Head TA for Spring 2023)
  <br>
</font>
<font size="3">
  <p style="margin-left: 25px;">
    <span style="color: gray;">
      Foundations of circuit theory-electric fields, magnetic fields, transmission lines, and Maxwell's equations, with engineering applications.
    </span>
  </p>
</font> -->

<!-- <br> -->

<div class="clustermaps-widget">
<script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ecf4d6&w=a&t=tt&d=_uUi94cpmcNCyRUHW_7GZIypCW8NCGmk_sE5ee3tpvc&co=265073&ct=ffffff&cmo=2d9596&cmn=9ad0c2'></script> 
</div>


<!-- https://clustrmaps.com/site/1bxh8 --> 

  </div> <!-- End publicationsContainer -->
</section> <!-- End publications-section -->

<script>
// Publication Search and Sort Functionality
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('publicationSearch');
  const sortSelect = document.getElementById('sortBy');
  const clearButton = document.getElementById('clearSearch');
  const publicationsContainer = document.getElementById('publicationsContainer');
  
  let publications = Array.from(document.querySelectorAll('.publication'));
  
  // Search functionality
  function filterPublications() {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredPublications = publications.filter(pub => {
      const title = pub.dataset.title.toLowerCase();
      const venue = pub.dataset.venue.toLowerCase();
      const year = pub.dataset.year;
      const authors = pub.querySelector('.publication-authors').textContent.toLowerCase();
      const abstract = pub.querySelector('.publication-abstract').textContent.toLowerCase();
      
      return title.includes(searchTerm) || 
             venue.includes(searchTerm) || 
             year.includes(searchTerm) || 
             authors.includes(searchTerm) || 
             abstract.includes(searchTerm);
    });
    
    displayPublications(filteredPublications);
  }
  
  // Sort functionality
  function sortPublications() {
    const sortBy = sortSelect.value;
    let sortedPublications = [...publications];
    
    switch(sortBy) {
      case 'date':
        sortedPublications.sort((a, b) => parseInt(b.dataset.year) - parseInt(a.dataset.year));
        break;
      case 'date-old':
        sortedPublications.sort((a, b) => parseInt(a.dataset.year) - parseInt(b.dataset.year));
        break;
      case 'title':
        sortedPublications.sort((a, b) => a.dataset.title.localeCompare(b.dataset.title));
        break;
      case 'venue':
        sortedPublications.sort((a, b) => a.dataset.venue.localeCompare(b.dataset.venue));
        break;
    }
    
    displayPublications(sortedPublications);
  }
  
  // Display publications
  function displayPublications(pubs) {
    publicationsContainer.innerHTML = '';
    pubs.forEach(pub => {
      publicationsContainer.appendChild(pub);
    });
  }
  
  // Event listeners
  searchInput.addEventListener('input', filterPublications);
  sortSelect.addEventListener('change', sortPublications);
  
  clearButton.addEventListener('click', function() {
    searchInput.value = '';
    filterPublications();
  });
  
  // Keyboard accessibility
  searchInput.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      searchInput.value = '';
      filterPublications();
    }
  });
});
</script>

<!-- <script type="text/javascript" src="//rf.revolvermaps.com/0/0/8.js?i=552rn9jpev6&amp;m=7&amp;c=186f65&amp;cr1=b5cb99&amp;f=arial&amp;l=49" async="async"></script> -->
