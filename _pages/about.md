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
      div.pub {
        line-height: 120%;
      }

      .publication {
        <!-- display: grid; /* Use grid display for layout */
        grid-template-columns: 150px 1fr; /* Two columns: 150px for image, 1fr for text */ -->
        align-items: flex-start; /* Align items to the top */
        <!-- gap: 10px; /* Add some gap between image and text */ -->
        margin-bottom: 5px;
      }

      .publication-image {
        margin-right: 10px;
        width: 150px; /* Set a fixed width for the image container */
        height: 150px; /* Set a fixed height for the image container */
        overflow: hidden; /* Hide any overflowing content within the container */
      }

      .publication-image img {
        width: 100%; /* Ensure the image fills the container horizontally */
        height: 100%; /* Ensure the image fills the container vertically */
        object-fit: cover; /* Maintain aspect ratio and crop if necessary */
      }

      .publication-details {
        display: inline-block;
        vertical-align: top;
        flex-grow: 1; /* Expand to fill available space */
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

<p align="justify">
  <font size="3" style="font-family: Noto Sans;">
    I am a PhD candidate in the Department of Electrical Engineering at Caltech, advised by 
    <a href="https://biophot.caltech.edu/" style="text-decoration: none;">
      <span style="color: #EC8F5E;"> Prof. Changhuei Yang.</span>
    </a>
    My current research interests include: 
    <br>
    <p style="margin-left: 25px;">
      (a) Computational microscopy for label-free imaging; 
      <br>
      (b) Hardware and software co-deisgn for biomedical applications.
    </p> 
    My aspiration is to become an engineer-scientist who advances scientific discovery through innovative engineering designs.
  </font>
</p>

<br>
<font size="5">
  <strong>
    News
  </strong>
</font>
<br>
<font size="3" style="font-family: Noto Sans;">

  12/03/2024 - I am awarded Schmidt Academy for Software Engineering Graduate Research Fellowship. The support will start on Jan. 2025 for contributions to the algorithm and software development towards computational microscopy, specifically Fourier Ptychographic Microscopy. 
  <a href="https://sase.caltech.edu/people/gra-fellows.html" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">[Schmidt Academy GRA Fellows]</span>
    </strong>
  </a>
  <br>
  08/06/2024 - Our new paper titled "Investigating 3D microbial community dynamics of the rhizosphere using quantitative phase and fluorescence microscopy" is online at <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2403122121" style="text-decoration: none;">
    <strong>
      <span style="color: #B2533E;">PNAS</span>
    </strong>
  </a>. 
  <a href="https://www.science.org/doi/10.1126/science.adt0513" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">[Science.org News]</span>
    </strong>
  </a>
  <br>
  05/24/2024 - I am awarded <strong> SPIE Optics and Photonics Scholarship </strong>. <a href="https://spie.org/membership/student-hub/scholarships/optics-and-photonics-education-scholarships/current-winners#_=_" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">[Webpage]</span>
    </strong>
    </a> 
  <a href="/files/Haowen Zhou PR24.pdf" style="text-decoration: none;">
    <strong>
      <span style="color: #B2533E;">[PDF]</span>
    </strong>
  </a>
  <a href="https://www.ee.caltech.edu/news/haowen-zhou-awarded-spie-optics-and-photonics-scholarship" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">[News]</span>
    </strong>
  </a>
  <br> 
  03/06/2024 - The new paper "AI-guided histopathology predicts brain metastasis in lung cancer patients" has been featured on the Caltech homepage. <a href="https://www.caltech.edu/about/news/using-ai-to-predict-the-spread-of-lung-cancer/" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">News</span>
    </strong>
    </a>
  <br>
  03/04/2024 - My new paper on "AI-guided histopathology predicts brain metastasis in lung cancer patients" is online today. Check my publication list <a href="https://hwzhou2020.github.io/publications/" style="text-decoration: none;">
    <strong>
      <span style="color: #186F65;">here</span>
    </strong>
    </a>!
  <br>
  02/14/2024 - I passed my candidacy exam!
  <br>
  11/21/2023 - My personal homepage is online!
  <br>
  06/30/2021 - I joined Caltech Biophotonics Lab! 
</font>

<br>
<br>
<font size="5">
  <strong>
    Selected Publications
  </strong>
</font>
<br>
<font size="3">
  Full publication list 
  <a href="https://hwzhou2020.github.io/publications/" style="text-decoration: none;">
    <strong>
      <span style="color: #435585;">here</span>
    </strong>
  </a>
</font>
<br>
<br>

<!-- pub 11 -->
<div class="publication">
  <!-- <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/FPM-INR.png" width="150" height="150">
  </div> -->
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
        &nbsp; &nbsp;  <span style="color: #186F65;">[Project Page]</span>
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

<!-- pub 17 -->
<div class="publication">
  <!-- <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/FPM-INR.png" width="150" height="150">
  </div> -->
  <div class="publication-details">
    <font size="4">
      <a href="https://arxiv.org/pdf/2405.10463" style="text-decoration: none;">
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
      <span style="color: #B2533E;">Advanced Photonics (In press), 2025</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/SVF.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
      <a href="https://hwzhou2020.github.io/SVF-Web/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #186F65;">[Project Page]</span>
      </a>
      <a href="https://osf.io/4a5ws/" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #FCE09B;">{Data}</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Single-shot volumetric fluorescence (SVF) imaging captures biological processes with high temporal resolution and a large field of view, unlike traditional methods requiring multiple axial plane scans. Existing SVF methods often face limitations due to large, complex point spread functions (PSFs), affecting signal-to-noise ratio, resolution, and field of view. The paper introduces the QuadraPol PSF combined with neural fields, using a compact custom polarizer and a polarization camera to detect fluorescence and encode the 3D scene within a compact PSF without depth ambiguity. This approach, coupled with a novel reconstruction algorithm, significantly reduces acquisition time by approximately 20 times and captures a 100 mm³ volume in one shot, demonstrated through imaging bacterial colonies and plant root morphology.
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/SVF_cover.jpg">

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

<font size="3">
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

<!-- <script type="text/javascript" src="//rf.revolvermaps.com/0/0/8.js?i=552rn9jpev6&amp;m=7&amp;c=186f65&amp;cr1=b5cb99&amp;f=arial&amp;l=49" async="async"></script> -->
