<h2> Awesome Public Medical Imaging Datasets </h2>


***Under construction: This list is being actively updated with additional datasets.***




## Table of Contents

- [Introduction](#introduction)
- [Head and Neck](#head-and-neck)
  - [Brain](#brain)
  - [Eyes](#eyes)
  - [Ears, Nose, and Throat](#ears-nose-and-throat)
- [Chest and Abdomen](#chest-and-abdomen)
  - [Heart and Blood Vessels](#heart-and-blood-vessels)
  - [Lungs](#lungs)
  - [Liver](#liver)
  - [Breast](#breast)
  - [Kidneys and Urinary Tract](#kidneys-and-urinary-tract)
- [Musculoskeletal System](#musculoskeletal-system)
  - [Bones](#bones)
  - [Joints](#joints)
  - [Muscles](#muscles)
- [Pelvis and Reproductive Organs](#pelvis-and-reproductive-organs)
  - [Female Reproductive Organs](#female-reproductive-organs)
  - [Male Reproductive Organs](#male-reproductive-organs)
- [Other Organs and Systems](#other-organs-and-systems)

## Introduction

This repository is a collection of publicly available medical imaging datasets. It aims to provide a comprehensive and valuable resource for researchers, healthcare professionals, and developers working in the field of medical imaging analysis.


- ![Leaderboard](src/leaderboard.png) The link of leaderboard.
- ![paper](src/paper.png) The link of related papers.

______

## Head and Neck

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=19726546"> **CT Lymph nodes** </a>
90 CTs dataset of lymph nodes
***Keyboard:*** CT scan, Lymph node detection
- <a href="https://lnq2023.grand-challenge.org"> **LNQ2023** </a> (Mediastinal Lymph Node Quantification)
Segmentation of Heterogeneous CT Data
***Keyboard:*** CT scan, Lymph node, Cancer
<a href="https://lnq2023.grand-challenge.org/evaluation/validation/leaderboard/"> ![Leaderboard](src/leaderboard.png) </a>
- <a href="https://huggingface.co/datasets/andreped/LyNoS"> **LyNoS** </a>
15 CTs with corresponding lymph nodes, azygos, esophagus, and subclavian carotid arteries
***Keyboard:*** CT scan, Lymph node, Segmentation
<a href="https://www.tandfonline.com/doi/full/10.1080/21681163.2022.2043778"> ![paper](src/paper.png) </a>



### Brain

- <a href="https://caddementia.grand-challenge.org"> **CADDementia** </a> (Computer-Aided Diagnosis of Dementia)
***Keyboard:*** Alzheimer's disease (AD), MRI
<a href="https://caddementia.grand-challenge.org/results_all"> ![Leaderboard](src/leaderboard.png) </a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811915000737"> ![paper](src/paper.png) </a> | <a href="https://caddementia.grand-challenge.org/Publications"> ![paper](src/paper.png) </a>

- <a href="https://www.nitrc.org/projects/ibsr/"> **IBSR** </a> (Internet Brain Segmentation Repository)
Manually-guided expert segmentation results along with magnetic resonance brain image data
***Keyboard:*** MRI, Labeled
- <a href="https://mindboggle.info/data.html"> **Mindboggle** </a>
Manually labeled human brain image data.
***Keyboard:*** MRI, Labeled
<a href="https://www.frontiersin.org/articles/10.3389/fnins.2012.00171/full"> ![paper](src/paper.png) </a> 
- <a href="https://valdo.grand-challenge.org"> **VALDO** </a> (VAscular Lesions DetectiOn)
***Keyboard:*** MRI, cerebral small vessel disease (CSVD), Labeled
<a href="https://zenodo.org/records/4600654"> ![paper](src/paper.png) </a>

### Eyes

- <a href="https://drive.grand-challenge.org"> **DRIVE** </a> (Digital Retinal Images for Vessel Extraction)
***Keyboard:*** Retinal, Segmentation
<a href="https://drive.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png) </a> 

- <a href="https://projects.ics.forth.gr/cvrl/fire"> **FIRE** </a> (Fundus Image Registration Dataset)
***Keyboard:*** Retinal, Labeled

- <a href="https://idrid.grand-challenge.org/"> **IDRiD** </a> (Indian Diabetic Retinopathy Image Dataset)
<a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841519301033?via%3Dihub"> ![paper](src/paper.png) First Results and Analysis </a>  | <a href="https://www.mdpi.com/2306-5729/3/3/25"> ![paper](src/paper.png) Data Descriptor </a> 



- <a href="https://github.com/SaharAlmahfouzNasser/MeDAL-Retina"> **MeDAL Retina Dataset** </a> 
***Keyboard:*** Retinal, Labeled
<a href="https://arxiv.org/pdf/2307.10698.pdf"> ![paper](src/paper.png) Comprehensive details </a> 



### Ears, Nose, and Throat

- <a href="https://empire10.grand-challenge.org"> **EMPIRE10** </a> (Evaluation of Methods for Pulmonary Image Registration 2010)
***Keyboard:*** CT, Registration of thoracic
<a href="https://pubmed.ncbi.nlm.nih.gov/21632295"> ![paper](src/paper.png) </a> 


______

## Chest and Abdomen

### Heart and Blood Vessels

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagealcapa"> **CardiacUDA** </a> (Unsupervised Domain Adaption)
***Keyboard:*** Echocardiogram Videos
<a href="https://arxiv.org/abs/2309.11145"> ![paper](src/paper.png) </a>
- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagealcapa"> **ImageALCAPA** </a> (Anomalous left coronary artery from pulmonary artery)
30 3D CTA images.
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Segmentation 
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0895611123001052"> ![paper](src/paper.png) </a>
- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagecas"> **ImageCAS** </a> (Coronary Artery Segmentation)
30 3D CTA images.
A Dataset and for Coronary Artery Segmentation based on CT.
***Keyboard:*** CTA (Computed tomography angiography), Segmentation 
<a href="https://ieeexplore.ieee.org/document/9994951"> ![paper](src/paper.png) </a>
- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagechd"> **ImageCHD** </a> (Congenital Heart Disease)
A 3D CT Image Dataset for classification of Congenital Heart Disease.
***Keyboard:*** CT scan, Labeled
<a href="https://arxiv.org/abs/2101.10799"> ![paper](src/paper.png) </a> 
- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagetbad"> **ImageTBAD** </a>
A 3D CT Image Dataset for Automatic Segmentation of of Type-B Aortic Dissection.
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Aorta
<a href="https://www.frontiersin.org/articles/10.3389/fphys.2021.732711/full"> ![paper](src/paper.png) </a> 
- <a href="https://multicenteraorta.grand-challenge.org/"> **SEG.A. 2023** </a> (Segmentation of the Aorta)
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Aorta
<a href="https://multicenteraorta.grand-challenge.org/evaluation/preliminary-phase/leaderboard/"> ![Leaderboard](src/leaderboard.png) </a> 

### Lungs

- <a href="https://anode09.grand-challenge.org/"> **ANODE09** </a> (Automatic Nodule Detection 2009)
Automatic detection of pulmonary nodules in chest
***Keyboard:*** CT-scan
<a href="https://anode09.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png) </a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841510000587"> ![paper](src/paper.png) </a> 

- <a href="https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community"> **ChestX-ray8** </a> (ChestXray-NIHCC)
100,000 anonymized chest x-ray images
***Keyboard:*** X-ray, Labeled
<a href="https://arxiv.org/abs/1705.02315"> ![paper](src/paper.png) </a> 

- <a href="https://stanfordmlgroup.github.io/competitions/chexpert/"> **CheXpert** </a>
A Large Chest X-Ray Dataset.
***Keyboard:*** X-ray, Labeled
<a href="https://arxiv.org/abs/1901.07031"> ![paper](src/paper.png) </a>

- <a href="https://crass.grand-challenge.org"> **CRASS12** </a> (Chest Radiograph Anatomical Structure Segmentation)
Automatic segmentation of anatomical structures in chest radiographs
<a href="https://www.diagnijmegen.nl/publications/hoge12/?bibkey=Hoge12"> ![paper](src/paper.png) </a> 

- <a href="https://luna16.grand-challenge.org"> **LUNA16** </a> (LUng Nodule Analysis 2016)
Nodule location detection
***Keyboard:*** Cancer, CT-scan
<a href="https://luna16.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png) </a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841517301020"> ![paper](src/paper.png) Overview paper </a> 

- <a href="https://vessel12.grand-challenge.org/"> **VESSEL12** </a> (VESsel SEgmentation in the Lung 2012)
Automatic (and semi-automatic) segmentation of blood vessels in the lungs from CT images
***Keyboard:*** CT-scan
<a href="https://vessel12.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png) </a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S136184151400111X"> ![paper](src/paper.png) Overview paper </a> 



### Liver

- <a href="https://competitions.codalab.org/competitions/17094"> **LiTS** </a> (Liver Tumor Segmentation)
***Keyboard:*** CT scan, Labeled
<a href="https://competitions.codalab.org/competitions/17094#results"> ![Leaderboard](src/leaderboard.png) </a> | <a href="https://arxiv.org/abs/1901.04056"> ![paper](src/paper.png) </a>



### Breast

- <a href="https://tdsc-abus2023.grand-challenge.org"> **MITOS-ATYPIA-14** </a>
It is made up of two parts: Detection of mitosis on the one hand, and evaluation of nuclear atypia score on the other hand.
***Keyboard:*** Cancer, Haematoxylin and eosin (H&E) stained slides
<a href="https://mitos-atypia-14.grand-challenge.org/Results2"> ![Leaderboard](src/leaderboard.png) </a>

- <a href="https://tdsc-abus2023.grand-challenge.org"> **TDSC-ABUS2023** </a> (Tumor Detection, Segmentation and Classification Challenge on Automated 3D Breast Ultrasound 2023)
***Keyboard:*** Ultrasound, Cancer, Labeled
<a href="https://tdsc-abus2023.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png) </a>


### Kidneys and Urinary Tract

- <a href="https://kits19.grand-challenge.org/"> **KiTS19** </a> (Kidney Tumor Segmentation 2019)
***Keyboard:*** CT scan, Cancer, Labeled
<a href="https://kits19.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png) </a>

______

## Musculoskeletal System

### Bones
- <a href="http://spineweb.digitalimaginggroup.ca/"> **SpineWeb** </a>
16 spinal imaging datasets

### Joints

### Muscles

_______

## Pelvis and Reproductive Organs

### Female Reproductive Organs

### Male Reproductive Organs
- <a href="https://pi-cai.grand-challenge.org/"> **PI-CAI** </a> (Prostate Imaging: Cancer AI)
***Keyboard:*** Prostate, MRI, Cancer, Labeled
<a href="https://pi-cai.grand-challenge.org/evaluation/open-development-phase/leaderboard/"> ![Leaderboard](src/leaderboard.png) </a>
______
## Other Organs and Systems

__________________


