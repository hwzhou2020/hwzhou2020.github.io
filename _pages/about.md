---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<html>
<head>
<style>
div.pub {
  line-height: 120%;
}

.publication {
  display: grid; /* Use grid display for layout */
  grid-template-columns: 150px 1fr; /* Two columns: 150px for image, 1fr for text */
  align-items: flex-start; /* Align items to the top */
  gap: 10px; /* Add some gap between image and text */
  margin-bottom: 45px;
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

<font size="4">
  I am a third year graduate student in the Department of Electrical Engineering at Caltech, supervised by 
  <a href="https://biophot.caltech.edu/" style="text-decoration: none;">
    <span style="color: #435585;"> Prof. Changhuei Yang.</span>
  </a>
  My current research involves two directions. 
  <br>
  <p style="margin-left: 25px;">
    (a) Computational microscopy with model-based and/or learning-based methods for biological and clinical applications;
  </p>
  <p style="margin-left: 25px;">
    (b) Deep learning enabled methods for digital pathology.
  </p> 
</font>
<br>
<br>
<font size="4">
    I am particularly interested in exploring how microscope systems, algorithms, and scientific applications interconnect.
</font>



Education and Selected Fellowships
------

**California Insitute of Technology (2021 - )**
- [Naren and Vinita Gupta Fellows (2022)](https://s2i.caltech.edu/people/fellows)

**University of Dayton (2019 - 2021)**
- [Dean's Fellow (2019)](https://udayton.edu/engineering/departments/electrooptics_grad/_resources/newsletters/2020-spring-newsletter.pdf)


**Huazhong University of Science and technology (2015 - 2019)**
- National Endeavor Scholarship Award of China (2016)


Selected Publications
------

Full publication list at 
<a href="https://hwzhou2020.github.io/publications/" style="text-decoration: none;">
  <span style="color: #435585;">here</span>
</a>


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
        Fourier ptychographic microscope faces challenges with long image stack reconstruction time and huge data volumes. We designed physics-based neural signal representations to tackle these challenges and facilitates remote diagnosis, and efficient data packaging.
      </span>
    </font>
  </div>
</div>


Teaching
======
Caltech EE151 - Electromagnetic Engineering (Spring 2023)