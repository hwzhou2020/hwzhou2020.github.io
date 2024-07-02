---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
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


<!-- pub 13 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Can_DL.png" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1364/OE.527986" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            13. Can deep neural networks work with amplitude and phase input of defocused images?
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Siyuan Yin, Ruizhi Cao, Mingshu Liang, Cheng Shen, <span style="color: #213555;"><strong>Haowen Zhou*,</strong></span> Oumeng Zhang, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Optics Express, 2024</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Can_DL.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We assess the feasibility of employing neural networks to directly process full amplitude and phase data from a defocus plane without digital refocusing. Our specific focus lies in understanding the tolerance for defocus in image classification neural networks when amplitude and phase are taken as inputs.
      </span>
    </font>
  </div>
</div>

<!-- pub 12 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/AI_NSCLC.png" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href=" https://doi.org/10.1002/path.6263" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            12. AI-guided histopathology predicts brain metastasis in lung cancer patients
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
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Brain metastases can occur in nearly half of patients with early and locally advanced (stage I–III) non-small cell lung cancer (NSCLC). There are no reliable histopathologic or molecular means to identify those who are likely to develop brain metastases. We sought to determine if deep learning could be applied to routine H&E-stained primary tumor tissue sections from stage I–III NSCLC patients to predict the development of brain metastasis.
      </span>
    </font>
  </div>
</div>

<!-- pub 11 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/FPM-INR.png" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1364/OPTICA.505283" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            11. FPM-INR: Fourier ptychographic microscopy image stack reconstruction using implicit neural representations
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
        Fourier ptychographic microscope faces challenges with long image stack reconstruction time and huge data volumes. We designed physics-based neural signal representations to tackle these challenges and facilitates remote diagnosis, and efficient data packaging.
      </span>
    </font>
  </div>
</div>


<!-- pub 10 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Automatic_detection.png" alt="Automatic_detection" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1038/s41598-023-32955-0" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            10. Automatic detection of circulating tumor cells and cancer associated fibroblasts using deep learning
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Cheng Shen, Siddarth Rawal, Rebecca Brown, <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Ashutosh Agarwal, Mark A. Watson, Richard J. Cote, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Sci. Rep., 2022</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Automatic_detection.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We build an all-in-focus fluorescent microscope for circulating tumor cells and cancer-associated fibroblasts detections. The system outperforms the commercialized microscope systems and achieves high performances in cell counting.
      </span>
    </font>
  </div>
</div>


<!-- pub 9 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Analysis_of.png" alt="Anlysis_of" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1117/1.OE.61.7.073102" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            9. Analysis of postreconstruction digital refocusing in Fourier ptychographic microscopy
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
         <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Cheng Shen, Mingshu Liang, Changhuei Yang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Opt. Eng., 2022</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Analysis_of.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We applied a thorough analysis in digital refocusing mechanism for Fourier ptychographic microscopy. It explains why a simple propagation physical model cannot succeed in a post-reconstrution manner.
      </span>
    </font>
  </div>
</div>


<!-- pub 8 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Dual_wave.png" alt="Dual_wave" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://www.light-am.com/article/pdf/preview/LAM2021090033.pdf" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            8. A review of the dual-wavelength technique for phase imaging and 3D topography
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
         <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Mallik Hussain, Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Light Adv. Manuf., 2022</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Dual_wave.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We surveyed dual-wavelength technique in phase imaging and 3D topography and summarized the current challenges in this field.
      </span>
    </font>
  </div>
</div>


<!-- pub 7 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Non_recursive.png" alt="Non_recursive" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-61-5-B190" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            7. Non-recursive transport of intensity phase retrieval with the transport of phase
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
         <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Haiyun Guo, Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;"> 
        <span style="color: #B2533E;">Appl. Opt., 2022</span>
      </a>
      <a> &nbsp; &nbsp;
        <span style="color: #186F65;"><strong>Editor's Pick</strong> </span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Non_recursive.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Transport of phase equation is a twin equation with transport of intensity equation, derived from the Helmholtz equation. The two equations can demonstrate the entire complex optical field and help amplitude-phase imaging.  
      </span>
    </font>
  </div>
</div>


<!-- pub 6 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Use_of.png" alt="Use_of" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-61-5-B314" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            6. Use of structured light in 3D reconstruction of transparent objects
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Haiyun Guo, <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Appl. Opt., 2022</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Use_of.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        A simple concept of light refraction due to a change of refractive index and curvature of the interface provides a straightforward way to reconstruct transparent phase objects with projected structured light. 
      </span>
    </font>
  </div>
</div>


<!-- pub 5 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Performance_analysis.png" alt="Performance" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-60-4-A73" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            5. Performance analysis of phase retrieval using transport of intensity with digital holography [Invited]
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Elena Stoykova, Mallik Hussain, Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Appl. Opt., 2021</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Performance_analysis.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Transport of intensity equation can facilitate wrapping free phase retrieval for digital holography. We compares its performance with traditional off-axis single- and dual-wavelength techniques. 
      </span>
    </font>
  </div>
</div>

<!-- pub 4 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Single_shot.png" alt="Single_shot" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-60-4-A84" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            4. Single-shot digital phase-shifting Moiré patterns for 3D topography
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Haiyun Guo, <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
        <a style="text-decoration: none;">
          <span style="color: #B2533E;">Appl. Opt., 2021</span>
        </a>
        <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Single_shot.txt" style="text-decoration: none;">
          &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
        </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We demonstrates a simple and robust technique of Moiré topography with single-image capture and incorporating digital filtering along with a four-step digitally implemented phase-shifting method for 3D surface mapping.
      </span>
    </font>
  </div>
</div>


<!-- pub 3 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Digital_corr.png" alt="Digital_corr" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-58-34-G177" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            3. Digital correlation of computer-generated holograms for 3D face recognition
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Xiaomeng Sui, Liangcai Cao, Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Appl. Opt., 2019</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Digital_correlation.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        A digital correlation method of a computer-generated hologram (CGH) can encode 3D spatial data information into a 2D hologram. We demonstrate its application in for 3D face recognition.
      </span>
    </font>
  </div>
</div>


<!-- pub 2 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/3D_obj.png" alt="3D_obj" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://opg.optica.org/ao/abstract.cfm?URI=ao-58-34-G197" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            2. 3D object recognition through processing of 2D holograms
          </strong>
        </span>
        </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Behzad Bordbar, <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Partha P. Banerjee
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;">Appl. Opt., 2019</span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/3D_object.txt" style="text-decoration: none;">
        &nbsp; &nbsp;  <span style="color: #B5CB99;">(BibTex)</span>
      </a>      
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        Digitally recorded holograms encode three-dimensional obejct information into a 2D images (hologram). This work demonstrates the correlation of the holograms as metric to reveal object topographic features.
      </span>
    </font>
  </div>
</div>


<!-- pub 1 -->
<div class="publication">
  <div class="publication-image">
    <img src="https://raw.githubusercontent.com/hwzhou2020/hwzhou2020.github.io/master/_publications/Sulfur.png" alt="Sulfur" width="150" height="150">
  </div>
  <div class="publication-details">
    <font size="4">
      <a href="https://doi.org/10.1039/C8TA02036A" style="text-decoration: none;">
        <span style="color: #191717;">
          <strong>
            1. Sulfur dioxide gas-sensitive materials based on zeolitic imidazolate framework-derived carbon nanotubes
          </strong>
        </span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: #A4907C;">
        Qun Li*, Jiabin Wu*, Liang Huang, Junfeng Gao, <span style="color: #213555;"><strong>Haowen Zhou,</strong></span> Yijie Shi, Qinhe Pan, Gang Zhang, Yu Du, Wenxi Liang
      </span>
    </font>
    <br>
    <font size="3" style="font-family: 'Font', Calibri;">
      <a style="text-decoration: none;">
        <span style="color: #B2533E;"> J. Mater. Chem. A, 2018 </span>
      </a>
      <a href="https://github.com/hwzhou2020/hwzhou2020.github.io/blob/master/_publications/Sulfur_dioxide_gas-sensitive.txt" style="text-decoration: none;">
        &nbsp; &nbsp; <span style="color: #B5CB99;">(BibTex)</span>
      </a>
    </font>
    <br>
    <font size="3">
      <span style="color: gray;">
        We demonstrate the synthesis of gas-sensing materials for sulfur dioxide (ZIF-67), which results in significant sensitivity, cross-selectivity and durability towards SO2 at room temperature.
      </span>
    </font>
  </div>
</div>


<font size="2">
  <br>
  <span style="color: gray;">
    Updated on July 02, 2024
  </span>
</font>




<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/citations?user=feZDslgAAAAJ&hl=en}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %} -->

<!-- {% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->
