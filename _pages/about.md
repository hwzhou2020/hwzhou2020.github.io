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
  display: grid; /* Use grid display for layout */
  grid-template-columns: 150px 1fr; /* Two columns: 150px for image, 1fr for text */
  align-items: flex-start; /* Align items to the top */
  gap: 10px; /* Add some gap between image and text */
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

</style>
</head>
<body>

<font size="3" style="font-family: Noto Sans;">
  I am a third year graduate student in the Department of Electrical Engineering at Caltech, supervised by 
  <a href="https://biophot.caltech.edu/" style="text-decoration: none;">
    <span style="color: #2D9596;"> Prof. Changhuei Yang.</span>
  </a>
  My current research involves two directions. 
  <br>
  <p style="margin-left: 25px;">
    (a) Computational microscopy with model-based and/or learning-based methods for biological and clinical applications; 
    <br>
    (b) Deep learning enabled methods for digital pathology.
  </p> 
  I am particularly interested in exploring how microscope systems, algorithms, and scientific applications interconnect.
  <br>
  <br>
  In 2021, I joined Caltech EE program and was sponsored by Sensing to Intelligence (S2I) Fellowship as a member of 
  <a href="https://s2i.caltech.edu/people/fellows" style="text-decoration: none;">
    <span style="color: #265073;">Naren and Vinita Gupta Fellows (2022).</span>
  </a>
  <br>
  <br>
  Prior to Caltech, I received M.S. degree (Class of 2021) in Electro-Optics and Photonics at University of Dayton, Ohio, US, with full sponsor from 
  <a href="https://udayton.edu/engineering/departments/electrooptics_grad/_resources/newsletters/2020-spring-newsletter.pdf" style="text-decoration: none;">
    <span style="color: #265073;">Dean's Fellowship (2019).</span>
  </a>
  At Dayton, I was working on digital holography and phase retrieval, supervised by 
  <a href="https://udayton.edu/directory/engineering/electrical_and_computer/banerjee_partha.php" style="text-decoration: none;">
    <span style="color: #2D9596;">Prof. Partha P. Banerjee.</span>
  </a> 
  In 2020-2021, I also served as the president of 
  <a href="https://www.optica.org/about/" style="text-decoration: none;">
    <span style="color: #265073;">Optica</span>
  </a> 
  and 
  <a href="http://spie.org" style="text-decoration: none;">
    <span style="color: #265073;">SPIE</span>
  </a> 
  student chapter at University Dayton, contributing to the optics and photonics community.
  <br>
  <br>
  In 2019, I received B.E. degree in Optics from 
  <a href="https://english.hust.edu.cn/" style="text-decoration: none;">
    <span style="color: #265073;">Huazhong University of Science and Technology (HUST)</span>
  </a> 
  , Wuhan, China. In my undergraduate times, I worked on ultrafast dynamics and was supervised by 
  <a href="http://lud.wnlo.hust.edu.cn/index_en.htm" style="text-decoration: none;">
    <span style="color: #2D9596;">Prof. Wenxi Liang.</span>
  </a> 
</font>

<br>
<br>
<font size="5">
  <strong>
    Selected Publications
  </strong>
</font>
<br>
<font size="4">
  Full publication list 
  <a href="https://hwzhou2020.github.io/publications/" style="text-decoration: none;">
    <span style="color: #435585;">here</span>
  </a>
</font>
<br>
<br>
<!-- pub 11 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/FPM-INR.png" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <span style="color: #191717;">
        <strong>
          FPM-INR: Fourier ptychographic microscopy image stack reconstruction using implicit neural representations
        </strong>
      </span>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Brandon Y. Feng*, Haiyun Guo, Siyu Lin, Mingshu Liang, Christopher A. Metzler, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a href=" " style="text-decoration: none;">
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
        Fourier ptychographic microscope images the biological samples with high-resolution and large field-of-view simultaneously. However, this microscope faces challenges with long image stack reconstruction time and huge data volumes. The authors designed physics-based neural signal representations to tackle these challenges and showed potential in facilitating remote diagnosis, digital pathology, and efficient clinical data packaging..
      </span>
    </font>
  </div>
</div>
<img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/images/FPM-INR-Cover.jpg">

<br>
<br>
<font size="5">
  <strong>
    Teaching
  </strong>
</font>
<br>
<font size="3">
  Caltech EE151 - Electromagnetic Engineering (Spring 2023)
</font>
