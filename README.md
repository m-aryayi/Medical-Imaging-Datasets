<h2> Awesome Public Medical Imaging Datasets </h2>


<img src="https://upload.wikimedia.org/wikipedia/commons/3/3e/Under_construction_icon-red.svg" alt="Under Construction" height="22"> ***Under construction: This list is being actively updated with additional datasets.***




## Table of Contents

- [Introduction](#introduction)
- [Head and Neck](#head-and-neck)
  - [Brain](#brain)
  - [Ears, Nose, Teeth, and Throat](#ears-nose-teeth-and-throat)
  - [Eyes](#eyes)
- [Chest and Abdomen](#chest-and-abdomen)
  - [Bowel](#bowel)
  - [Breast](#breast)
  - [Heart and Blood Vessels](#heart-and-blood-vessels)
  - [Kidneys and Urinary Tract](#kidneys-and-urinary-tract)
  - [Liver](#liver)
  - [Lungs](#lungs)
- [Musculoskeletal System](#musculoskeletal-system)
  - [Bones](#bones)
  - [Joints](#joints)
- [Pelvis and Reproductive Organs](#pelvis-and-reproductive-organs)
  - [Female Reproductive Organs](#female-reproductive-organs)
  - [Male Reproductive Organs](#male-reproductive-organs)
- [Other Organs and Systems](#other-organs-and-systems)
  - [Lymph Nodes](#lymph-nodes)
- [Multi Oragns Datasets](#multi-organs-datasets)

## Introduction

This repository is a collection of publicly available medical imaging datasets. It aims to provide a comprehensive and valuable resource for researchers, healthcare professionals, and developers working in the field of medical imaging analysis.


- ![Leaderboard](src/leaderboard.png) The link of leaderboard.
- ![paper](src/paper.png) The link of related papers.

![NumberOfDataSet](src/numberOfDatasets.png)

______

## Head and Neck

### Brain

- <a href="https://atlas.grand-challenge.org"> **ATLAS R2.0**</a> (Anatomical Tracings of Lesions After Stroke) <br>
A larger dataset of T1w MRIs and manually segmented lesion masks <br>
***Keyboard:***  MRI, Segmentation, Labeled  <br>
<a href="https://atlas.grand-challenge.org/evaluation/lesion-segmentation-hidden-test-set/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.nature.com/articles/s41597-022-01401-7"> ![paper](src/paper.png)</a>

- <a href="https://bonbid-hie2023.grand-challenge.org"> **BONBID-HIE**</a> (BOston Neonatal Brain Injury Dataset for Hypoxic Ischemic Encephalopathy) <br>
***Keyboard:***  MRI, Segmentation, Labeled  <br>
<a href="https://bonbid-hie2023.grand-challenge.org/evaluation/development-stage/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.biorxiv.org/content/10.1101/2023.06.30.546841v1"> ![paper](src/paper.png)  Data Descriptor</a>

- <a href="https://brainptm-2021.grand-challenge.org"> **BrainPTM 2021**</a> (Brain Pre-surgical white matter Tractography Mapping) <br>
Data consists of 75 cases<br>
***Keyboard:*** MRI, Cancer, Segmentation, Labeled  <br>
<a href="https://brainptm-2021.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://cada.grand-challenge.org"> **CADA**</a> (Cerebral Aneurysm Detection and Analysis) <br>
Data of patients with cerebral aneurysms without vasospasm were collected for diagnostic and treatment decision purposes.<br>
***Keyboard:*** X-ray rotational angiography (3DRA), Segmentation, Labeled  <br>
<a href="https://cada.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841521003789"> ![paper](src/paper.png)</a>

- <a href="https://caddementia.grand-challenge.org"> **CADDementia**</a> (Computer-Aided Diagnosis of Dementia) <br>
***Keyboard:*** Alzheimer's disease (AD), MRI  <br>
<a href="https://caddementia.grand-challenge.org/results_all"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811915000737"> ![paper](src/paper.png)</a> | <a href="https://caddementia.grand-challenge.org/Publications"> ![paper](src/paper.png)</a>

- <a href="https://crossmoda.grand-challenge.org"> **crossMoDA 2021**</a> (Cross-Modality Domain Adaptation) <br>
The goal is to segment two key brain structures involved in the follow-up and treatment planning of vestibular schwannoma (VS): the tumour and the cochlea<br>
***Keyboard:*** MRI, Segmentation <br>
<a href="https://crossmoda.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://crossmoda2022.grand-challenge.org"> **crossMoDA 2022**</a> (Cross-Modality Domain Adaptation) <br>
The goal is to segment two key brain structures involved in the follow-up and treatment planning of vestibular schwannoma (VS): the tumour and the cochlea, and to automatically classify hrT2 images with VS according to the Koos grade<br>
***Keyboard:*** MRI, Segmentation <br>
<a href="https://crossmoda2022.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://feta.grand-challenge.org"> **FeTA**</a> (Fetal Tissue Annotation) <br>
A dataset of manually segmented pathological and non-pathological fetal magnetic resonance brain volume reconstructions across a range of gestational ages into different tissue categories <br>
***Keyboard:*** MRI, Labeled, Segmentation <br>
<a href="https://www.nature.com/articles/s41597-021-00946-3"> ![paper](src/paper.png)</a>

- <a href="https://www.nitrc.org/projects/ibsr/"> **IBSR**</a> (Internet Brain Segmentation Repository)  <br>
Manually-guided expert segmentation results along with magnetic resonance brain image data  <br>
***Keyboard:*** MRI, Labeled  <br>

- <a href="https://instance.grand-challenge.org"> **INSTANCE2022**</a> (INtracranial
hemorrhage SegmenTAtioN ChallengE) <br>
A training set of 100 cases with ground-truth and a validation set with 30 cases without ground-truth labels.<br>
***Keyboard:*** Intracranial hemorrhage (ICH), CT Scan, Labeled  <br>
<a href="https://instance.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2301.03281"> ![paper](src/paper.png)</a>

- <a href="https://isles22.grand-challenge.org"> **ISLES'22**</a> (Ischemic Stroke Lesion Segmentation) <br>
Multimodal MRI infarct segmentation in acute and sub-acute stroke<br>
***Keyboard:*** MRI <br>
<a href="https://isles22.grand-challenge.org/evaluation/preliminary-docker-evaluation/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://mindboggle.info/data.html"> **Mindboggle**</a>  <br>
Manually labeled human brain image data. <br>
***Keyboard:*** MRI, Labeled <br>
<a href="https://www.frontiersin.org/articles/10.3389/fnins.2012.00171/full"> ![paper](src/paper.png)</a>

- <a href="https://archive.norstore.no/pages/public/datasetDetail.jsf?id=10.11582/2017.00004"> **RESECT**</a> (REtroSpective Evaluation of Cerebral Tumors)  <br>
A clinical database of pre-oper, ative MRI and intra-operative ultrasound in low-grade glioma surgeries <br>
***Keyboard:*** Cancer, Registration, Labeled <br>
<a href="https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.12268"> ![paper](src/paper.png)</a>

- <a href="https://shifts.grand-challenge.org"> **Shifts Challenge 2022**</a><br>
White Matter Multiple Sclerosis (MS) lesion segmentation in 3D Magnetic Resonance Imaging (MRI) of the brain <br>
***Keyboard:*** MRI <br>
<a href="https://shifts.grand-challenge.org/evaluation/ms-lesion-segmentation-phase-i/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://slcn.grand-challenge.org"> **SLCN**</a> (Surface Learning for Clinical Neuroimaging)  <br>
Part of the <a href="http://www.developingconnectome.org"> dHCP</a> (Developing Human Connectome Project) <br>
***Keyboard:*** MRI <br>
<a href="https://slcn.grand-challenge.org/evaluation/preliminary-phase/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://topcow23.grand-challenge.org"> **TopCoW**</a> <br>
Topology-Aware Anatomical Segmentation of the Circle of Willis <br>
***Keyboard:*** Magnetic Resonance Angiography (MRA) and Computed Tomography Angiography (CTA) <br>
<a href="https://topcow23.grand-challenge.org/evaluation/validation-cta-multiclass/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2312.17670"> ![paper](src/paper.png)</a>

- <a href="https://valdo.grand-challenge.org"> **VALDO**</a> (VAscular Lesions DetectiOn)  <br>
***Keyboard:*** MRI, cerebral small vessel disease (CSVD), Labeled  <br>
<a href="https://zenodo.org/records/4600654"> ![paper](src/paper.png)</a>



### Ears, Nose, Teeth, and Throat

- <a href="https://dentex.grand-challenge.org"> **DENTEX**</a> <br>
Dental Enumeration and Diagnosis on Panoramic X-rays <br>
***Keyboard:*** X-rays, Labeled <br>
<a href="https://dentex.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2305.19112"> ![paper](src/paper.png)</a> | <a href="https://arxiv.org/abs/2303.06500"> ![paper](src/paper.png)</a>

- <a href="https://github.com/abenhamadou/3DTeethSeg22_challenge"> **3DTeethSeg22**</a> <br>
A total of 1800 3D intra-oral scan for 900 patients covering their upper and lower jaws separately.<br>
***Keyboard:***  Labeeld, Segmentation <br>
<a href="https://arxiv.org/abs/2305.18277"> ![paper](src/paper.png)</a> | <a href="https://arxiv.org/abs/2210.06094"> ![paper](src/paper.png)</a>

- <a href="https://zenodo.org/records/1473724"> **OpenEar**</a> <br>
A library consisting of eight three-dimensional models of the human temporal bone. <br>
***Keyboard:***  Cone Beam Computed Tomography (CBCT) <br>
<a href="https://www.nature.com/articles/sdata2018297"> ![paper](src/paper.png)</a>

- <a href="https://tn-scui2020.grand-challenge.org"> **TN-SCUI2020**</a> (Thyroid Nodule Segmentation and Classification in Ultrasound Images) <br>
A dataset of thyroid nodule with over 4,500 patient <br>
***Keyboard:***  Ultrasound Image, Thyroid <br>
<a href="https://tn-scui2020.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://ditto.ing.unimore.it/toothfairy"> **ToothFairy**</a> <br>
A dataset of dental scans obtained by 3D CBCT <br>
***Keyboard:***  Cone Beam Computed Tomography (CBCT), Segmentation <br>
<a href="https://toothfairy.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://link.springer.com/chapter/10.1007/978-3-031-43148-7_44"> ![paper](src/paper.png)</a>



### Eyes

- <a href="https://amd.grand-challenge.org"> **ADAM**</a> <br>
Diagnosis of Age-related Macular degeneration (AMD) and segmentation of lesions in fundus photos from AMD patients <br>
***Keyboard:*** Labeled  <br>
<a href="https://amd.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/9768802"> ![paper](src/paper.png)</a>

- <a href="https://age.grand-challenge.org"> **AGE**</a> (Angle closure Glaucoma Evaluation) <br>
A dataset of 4800 annotated AS-OCT images<br>
***Keyboard:*** OCT <br>
<a href="https://age.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/31036585"> ![paper](src/paper.png) Clinical Background</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841520301626"> ![paper](src/paper.png)</a>

- <a href="https://airogs.grand-challenge.org"> **AIROGS**</a> (Artificial Intelligence for RObust Glaucoma Screening) <br>
This dataset includes around 113,000 images from about 60,000 patients<br>
***Keyboard:*** Fundus Images <br>
<a href="https://airogs.grand-challenge.org/evaluation/preliminary-test-phase-1/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/abstract/document/10253652"> ![paper](src/paper.png) Summary Paper</a>

- <a href="https://cataracts.grand-challenge.org"> **CATARACTS**</a> <br>
Surgical tool detection in 50 videos of cataract surgeries<br>
***Keyboard:*** Video, Labeled  <br>
<a href="https://cataracts.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S136184151830865X"> ![paper](src/paper.png)</a>

- <a href="https://drac22.grand-challenge.org"> **DRAC 2022**</a> (Diabetic Retinopathy Analysis Challenge) <br>
A ultra-wide optical coherence tomography angiography (UW-OCTA) dataset addressing three primary clinical tasks: DR lesion segmentation, image quality assessment, and DR grading.<br>
***Keyboard:*** Diabetic retinopathy, Segmentation, Classification<br>
<a href="https://drac22.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2304.02389"> ![paper](src/paper.png)</a> | <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4593632"> ![paper](src/paper.png)</a>

- <a href="https://drive.grand-challenge.org"> **DRIVE**</a> (Digital Retinal Images for Vessel Extraction) <br>
***Keyboard:*** Retinal, Segmentation <br>
<a href="https://drive.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> 

- <a href="https://projects.ics.forth.gr/cvrl/fire"> **FIRE**</a> (Fundus Image Registration Dataset) <br>
***Keyboard:*** Retinal, Labeled

- <a href="https://aistudio.baidu.com/competition/detail/90/0/introduction"> **GAMMA**</a> <br>
The dataset consists of 2D fundus images and 3D optical coherence tomography (OCT) images of 300 patients. The dataset was annotated with glaucoma grade in every sample, and macular fovea coordinates as well as optic disc/cup segmentation mask in the fundus image. <br>
***Keyboard:*** OCT images <br>
<a href="https://aistudio.baidu.com/competition/detail/90/0/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2202.06511"> ![paper](src/paper.png)</a>

- <a href="https://idrid.grand-challenge.org/"> **IDRiD**</a> (Indian Diabetic Retinopathy Image Dataset) <br>
<a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841519301033?via%3Dihub"> ![paper](src/paper.png) First Results and Analysis</a>  | <a href="https://www.mdpi.com/2306-5729/3/3/25"> ![paper](src/paper.png) Data Descriptor</a> 

- <a href="https://justraigs.grand-challenge.org"> **JustRAIGS**</a> (Justified Referral in AI Glaucoma Screening) <br>
The dataset is divided into a training subset with 101,442 gradable fundus images, spanning both referable and no referable glaucomatous cases, and a test subset comprising 9,741 fundus images. <br>
***Keyboard:*** Fundus Images, Labeled  <br>
<a href="https://justraigs.grand-challenge.org/evaluation/development-phase/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/pii/S2666914523000325"> ![paper](src/paper.png)</a>

- <a href="https://github.com/SaharAlmahfouzNasser/MeDAL-Retina"> **MeDAL Retina Dataset**</a>  <br>
***Keyboard:*** Retinal, Labeled <br>
<a href="https://arxiv.org/pdf/2307.10698.pdf"> ![paper](src/paper.png) Comprehensive details</a> 

- <a href="https://odir2019.grand-challenge.org"> **ODIR 2019**</a> (Ocular Disease Intelligent Recognition) <br>
A database of 5000 patients with age, color fundus photographs from left and right eyes <br>
***Keyboard:*** Labeled<br>
<a href="https://odir2019.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://palm.grand-challenge.org"> **PALM**</a> <br>
Investigation and development of algorithms associated with the diagnosis of Pathological Myopia (PM) and segmentation of lesions in fundus photos from PM patients. <br>
***Keyboard:*** Labeled <br>
<a href="https://palm.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://ravir.grand-challenge.org"> **RAVIR**</a> <br>
A Dataset and Methodology for the Semantic Segmentation and Quantitative Analysis of Retinal Arteries and Veins in Infrared Reflectance Imaging <br>
<a href="https://ravir.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/abstract/document/9744459"> ![paper](src/paper.png)</a> | <a href="https://escholarship.org/uc/item/4r63v2bd"> ![paper](src/paper.png)</a>

- <a href="https://refuge.grand-challenge.org"> **REFUGE**</a> (Retinal Fundus Glaucoma) <br>
A data set of 1200 fundus images with ground truth segmentations and clinical glaucoma labels <br>
***Keyboard:*** Segmentation, Classification, Labeled <br>
<a href="https://refuge.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841519301100"> ![paper](src/paper.png)</a> | <a href="https://www.nature.com/articles/s41746-020-00329-9"> ![paper](src/paper.png)</a>

- <a href="https://retouch.grand-challenge.org"> **RETOUCH**</a> (Retinal OCT Fluid Challenge) <br>
Detect and segment various types of fluids on a common dataset of optical coherence tomography (OCT) volumes representing different retinal diseases, acquired with devices from different manufacturers. <br>
***Keyboard:*** OCT images <br>
<a href="https://retouch.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/8653407"> ![paper](src/paper.png)</a>

- <a href="https://riadd.grand-challenge.org"> **RFMiD**</a> (Retinal Fundus Multi-Disease Image Dataset) <br>
It consists of 3200 fundus images<br>
***Keyboard:*** Fundus Images, Classification <br>
<a href="https://riadd.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.mdpi.com/2306-5729/6/2/14"> ![paper](src/paper.png) Data Descriptor</a> 

- <a href="https://rocc.grand-challenge.org"> **ROCC**</a> (Retinal OCT Classification Challenge) <br>
A dataset of OCT volumes, acquired with Topcon SD-OCT devices <br>
***Keyboard:*** OCT images, Diabetic retinopathy <br>

- <a href="https://aistudio.baidu.com/competition/detail/1101/0/introduction"> **STAGE**</a> (Structural-Functional Transition in Glaucoma Assessment) <br>
400 OCT data and corresponding Visual Field test reports with Mean Deviation (MD) values, sensitivity maps and pattern deviation probability map labels. <br>
***Keyboard:*** OCT images <br>
<a href="https://aistudio.baidu.com/competition/detail/1101/0/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://cecas.clemson.edu/~ahoover/stare"> **STARE**</a> (STructured Analysis of the Retina) <br>
***Keyboard:*** Labeled <br>

______

## Chest and Abdomen


### Bowel

- <a href="https://conic-challenge.grand-challenge.org"> **CoNIC**</a> (Colon Nuclei Identification and Counting) <br>
***Keyboard:*** whole-slide images (WSI), Nuclear segmentation and classification <br>
<a href="https://conic-challenge.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2111.14485"> ![paper](src/paper.png)</a> 

- <a href="https://digestpath2019.grand-challenge.org"> **Digestpath2019**</a> (Digestive-System Pathological 2019)<br>
Colonoscopy tissue segmentation and classification and Signet ring cell detection dataset  <br>
***Keyboard:*** Whole slide image (WSI), Cancer, Labeled <br>
<a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841522001323"> ![paper](src/paper.png)</a> 

- <a href="https://endocv2021.grand-challenge.org"> **EndoCV2021**</a> (Endoscopy Computer Vision 2021)<br>
Addressing generalisability in polyp detection and segmentation <br>
***Keyboard:*** Colonoscopy, Labeled <br>

- <a href="https://paip2020.grand-challenge.org"> **PAIP2020**</a> <br>
Classification of molecular subtypes in colorectal cancer for whole-slide image analyses <br>
<a href="https://paip2020.grand-challenge.org/evaluation/validation/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://2023paip.grand-challenge.org"> **PAIP2023**</a> <br>
Tumor cellularity prediction in pancreatic cancer (supervised learning) and colon cancer (transfer learning) <br>
<a href="https://2023paip.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=3539213"> **The National CT Colonography Trial (ACRIN 6664)**</a> <br>
A collection contains 825 cases of CT colonography imaging with accompanying spreadsheets that provide polyp descriptions and their location within the colon segments. <br>
<a href="https://www.nejm.org/doi/full/10.1056/NEJMoa0800996"> ![paper](src/paper.png)</a> 




### Breast

- <a href="https://acrobat.grand-challenge.org"> **ACROBAT**</a> (AutomatiC Registration Of Breast cAncer Tissue) <br>
Consisting of 4212 WSIs from 1153 patients <br>
***Keyboard:*** whole-slide images (WSI), Cancer <br>
<a href="https://acrobat.grand-challenge.org/evaluation/model-development/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="http://arxiv.org/abs/2211.13621"> ![paper](src/paper.png)</a> 

- <a href="https://iciar2018-challenge.grand-challenge.org"> **BACH**</a> (BreAst Cancer Histology) <br>
***Keyboard:*** Biopsy, Cancer <br>
<a href="https://iciar2018-challenge.grand-challenge.org/evaluation/part-a/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841518307941"> ![paper](src/paper.png)</a>

- <a href="https://bci.grand-challenge.org"> **BCI**</a> (Breast Cancer Immunohistochemical) <br>
***Keyboard:*** hematoxylin and eosin (HE) stained images, Image Generation, Labeled <br>
<a href="https://bci.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="Breast Cancer Immunohistochemical"> ![paper](src/paper.png)</a>

- <a href="https://bcnb.grand-challenge.org"> **BCNB**</a> (Breast Cancer Core-Needle Biopsy) <br>
A dataset of Early Breast Cancer Core-Needle Biopsy WSI, which includes core-needle biopsy whole slide images of early breast cancer patients and the corresponding clinical data.  <br>
***Keyboard:***  Whole-Slide Images (WSIs), Labeled <br>
<a href="https://pubmed.ncbi.nlm.nih.gov/34722313"> ![paper](src/paper.png)</a>

- <a href="https://github.com/PathologyDataScience/BCSS"> **BCSS**</a> (Breast Cancer Semantic Segmentation) <br>
The dataset contains over 20,000 segmentation annotations of tissue region from breast cancer images from TCGA. <br>
***Keyboard:***  Cancer, Labeled <br>
<a href="https://academic.oup.com/bioinformatics/article/35/18/3461/5307750"> ![paper](src/paper.png)</a>

- <a href="https://breastpathq.grand-challenge.org/"> **BreastPathQ**</a> <br>
Development of quantitative biomarkers for the determination of cancer cellularity from whole slide images (WSI) of breast cancer hematoxylin and eosin (H&E) stained pathological slides <br>
***Keyboard:*** Cancer, Haematoxylin and eosin (H&E) stained slides <br>
<a href="https://breastpathq.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://ecdp2020.grand-challenge.org"> **HEROHE**</a> (HER2 on hematoxylin and eosin) <br>
The dataset consists of annotated, whole-slide images dataset (509), specifically collected for predicting human epidermal growth factor receptor 2 (HER2) status <br>
***Keyboard:*** whole-slide images (WSI), Cancer <br>
<a href="https://www.mdpi.com/2313-433X/8/8/213"> ![paper](src/paper.png)</a>

- <a href="https://imig.science/midog2021"> **MIDOG 2021**</a> (Mitosis Domain Generalization 2021) <br>
Detect mitotic figures (cells undergoing cell division) from histopathology images (object detection) <br>
***Keyboard:*** Whole-Slide Images (WSI), Cancer, Labeled <br>
<a href="https://midog2021.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841522003279"> ![paper](src/paper.png)</a> 

- <a href="https://imig.science/midog"> **MIDOG 2022**</a> (Mitosis Domain Generalization 2022) <br>
Detect mitotic figures (cells undergoing cell division) from histopathology images (object detection) <br>
***Keyboard:*** Whole-Slide Images (WSI), Cancer, Labeled <br>
<a href="https://midog2022.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2309.15589"> ![paper](src/paper.png)</a>

- <a href="https://tdsc-abus2023.grand-challenge.org"> **MITOS-ATYPIA-14**</a> <br>
It is made up of two parts: Detection of mitosis on the one hand, and evaluation of nuclear atypia score on the other hand. <br>
***Keyboard:*** Cancer, Haematoxylin and eosin (H&E) stained slides <br>
<a href="https://mitos-atypia-14.grand-challenge.org/Results2"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://sites.google.com/view/nucls"> **NuCLS**</a> <br>
The datasets contain over 220000 labeled nuclei from breast cancer images from TCGA <br>
***Keyboard:***  Cancer, Labeled <br>
<a href="https://arxiv.org/abs/2102.09099"> ![paper](src/paper.png)</a>

- <a href="https://tdsc-abus2023.grand-challenge.org"> **TDSC-ABUS2023**</a> (Tumor Detection, Segmentation and Classification Challenge on Automated 3D Breast Ultrasound 2023) <br>
***Keyboard:*** Ultrasound, Cancer, Labeled <br>
<a href="https://tdsc-abus2023.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://tiger.grand-challenge.org"> **TIGER**</a> (Tumor InfiltratinG lymphocytes in breast cancER) <br>
***Keyboard:***  H&E Whole-Slide Images (WSI), Cancer, Detecion, Segmentation <br>
<a href="https://tiger.grand-challenge.org/evaluation/segmentation-and-detection-public-test/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>




### Heart and Blood Vessels

- <a href="https://www.creatis.insa-lyon.fr/Challenge/acdc"> **ACDC**</a> (Automated Cardiac Diagnosis Challenge) <br>
The dataset contains data from 150 multi-equipments CMRI recordings with reference measurements and classification from two medical experts. <br>
***Keyboard:***  Cardiac MRI (CMR), Segmentation <br>
<a href="https://www.creatis.insa-lyon.fr/Challenge/acdc/results.html"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/29994302"> ![paper](src/paper.png)</a>

- <a href="https://arcade.grand-challenge.org"> **ARCADE**</a> <br>
Automatic Region-based Coronary Artery Disease Diagnostics Using X-Ray Angiography Images <br>
***Keyboard:***  X-ray coronary angiography, Labeled <br>
<a href="https://arcade.grand-challenge.org/evaluation/phase_1_segmentation_detection/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.nature.com/articles/s41597-023-02871-z"> ![paper](src/paper.png)</a>

- <a href="https://asoca.grand-challenge.org"> **ASOCA**</a> (Automated Segmentation of Coronary Arteries) <br>
A set of Cardiac Computed Tomography Angiography (CCTA) with contrast agent showing the coronary arteries <br>
***Keyboard:***  CCTA, Labeled <br>
<a href="https://asoca.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://camus.creatis.insa-lyon.fr/challenge"> **CAMUS**</a> (Cardiac Acquisitions for Multi-structure Ultrasound Segmentation) <br>
The dataset consists of clinical exams from 500 patients<br>
***Keyboard:***  2D echocardiographic images <br>
<a href="https://www.creatis.insa-lyon.fr/Challenge/camus/results.html"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/30802851"> ![paper](src/paper.png)</a>

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagealcapa"> **CardiacUDA**</a> (Unsupervised Domain Adaption) <br>
***Keyboard:*** Echocardiogram Videos <br>
<a href="https://arxiv.org/abs/2309.11145"> ![paper](src/paper.png)</a>

- <a href="https://www.creatis.insa-lyon.fr/Challenge/CETUS/"> **CETUS**</a> (Challenge on Endocardial Three-dimensional Ultrasound Segmentation) <br>
The dataset is composed of 45 sequences of 3D ultrasound volumes of one cardiac cycle from 45 patients to compare left ventricle segmentation methods for both End Diastolic and End Systolic phase instances.<br>
***Keyboard:***  Ultrasound imaging, Segmentation <br>
<a href="https://www.creatis.insa-lyon.fr/Challenge/CETUS/results.html"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://vessel-wall-segmentation-2022.grand-challenge.org"> **COSMOS**</a> (CarOtid vessel wall SegMentation and atherosclerOsis diagnosiS) <br>
***Keyboard:***  3D-VISTA (volume isotropic turbo spin echo acquisition) images <br>
<a href="https://vessel-wall-segmentation-2022.grand-challenge.org/evaluation/validation/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagealcapa"> **ImageALCAPA**</a> (Anomalous left coronary artery from pulmonary artery) <br>
30 3D CTA images. <br>
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Segmentation  <br>
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0895611123001052"> ![paper](src/paper.png)</a>

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagecas"> **ImageCAS**</a> (Coronary Artery Segmentation) <br>
A Dataset and for Coronary Artery Segmentation based on CT. <br>
***Keyboard:*** CTA (Computed tomography angiography), Segmentation  <br>
<a href="https://ieeexplore.ieee.org/document/9994951"> ![paper](src/paper.png)</a>

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagechd"> **ImageCHD**</a> (Congenital Heart Disease) <br>
A 3D CT Image Dataset for classification of Congenital Heart Disease. <br>
***Keyboard:*** CT scan, Labeled <br>
<a href="https://arxiv.org/abs/2101.10799"> ![paper](src/paper.png)</a> 

- <a href="https://www.kaggle.com/datasets/xiaoweixumedicalai/imagetbad"> **ImageTBAD**</a> <br>
A 3D CT Image Dataset for Automatic Segmentation of of Type-B Aortic Dissection. <br>
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Aorta <br>
<a href="https://www.frontiersin.org/articles/10.3389/fphys.2021.732711/full"> ![paper](src/paper.png)</a> 

- <a href="https://www.creatis.insa-lyon.fr/Challenge/myosaiq"> **MYOSAIQ**</a> (MYOcardial Segmentation with Automated Infarct Quantification)<br>
The full dataset is composed of 467 Late gadolinium enhanced magnetic resonance images from two different cohorts to quantify myocardial infarction (MI) lesions at different phases of the longitudinal evolution of the disease<br>
***Keyboard:*** MRI, Segmentation <br>

- <a href="https://www.ub.edu/mnms"> **M&Ms**</a> <br>
Multi-Centre, Multi-Vendor and Multi-Disease Cardiac Segmentation <br>
***Keyboard:***  Cardiac MRI (CMR)<br>
<a href="https://ieeexplore.ieee.org/document/9458279"> ![paper](src/paper.png)</a>

- <a href="https://www.ub.edu/mnms-2"> **M&Ms-2**</a> <br>
Multi-Disease, Multi-View & Multi-Center
Right Ventricular Segmentation in Cardiac MRI <br>
***Keyboard:***  Cardiac MRI (CMR)<br>
<a href="https://competitions.codalab.org/competitions/31559#results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/10103611"> ![paper](src/paper.png)</a>

- <a href="https://orcascore.grand-challenge.org"> **orCaScore**</a> <br>
Cardiac CT exams of 72 patients <br>
***Keyboard:*** CT scan <br>
<a href="https://orcascore.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/27147348"> ![paper](src/paper.png)</a>

- <a href="https://parse2022.grand-challenge.org"> **Parse2022**</a> (Pulmonary Artery Segmentation 2022) <br>
Our dataset contains 200 3D volumes with refined pulmonary artery label <br>
***Keyboard:*** CT Pulmonary Angiography (CTPA) <br>
<a href="https://parse2022.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2304.03708"> ![paper](src/paper.png)</a>

- <a href="https://multicenteraorta.grand-challenge.org"> **SEG.A. 2023**</a> (Segmentation of the Aorta) <br>
***Keyboard:*** CTA (Computed tomography angiography), Labeled, Aorta <br>
<a href="https://multicenteraorta.grand-challenge.org/evaluation/preliminary-phase/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> 



### Kidneys and Urinary Tract

- <a href="https://kipa22.grand-challenge.org"> **KiPA22**</a> (Kidney PArsing 2022) <br>
Multi-Structure Segmentation for Renal Cancer Treatment <br>
***Keyboard:*** Computed Tomography Angiography (CTA), Labeled <br>
<a href="https://kipa22.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://kits19.grand-challenge.org/"> **KiTS19**</a> (Kidney Tumor Segmentation 2019) <br>
***Keyboard:*** CT scan, Cancer, Labeled <br>
<a href="https://kits19.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841520301857"> ![paper](src/paper.png)</a>

- <a href="https://kits-challenge.org/kits21"> **KiTS21**</a> (Kidney Tumor Segmentation 2021) <br>
***Keyboard:*** CT scan, Cancer, Labeled <br>
<a href="https://kits21.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2307.01984"> ![paper](src/paper.png)</a> | <a href="https://link.springer.com/chapter/10.1007/978-3-030-98385-7_13"> ![paper](src/paper.png)

- <a href="https://kits-challenge.org/kits23"> **KiTS23**</a> (Kidney Tumor Segmentation 2023) <br>
***Keyboard:*** CT scan, Cancer, Labeled <br>


### Liver

- <a href="https://www.ircad.fr/research/data-sets/liver-segmentation-3d-ircadb-01"> **3D-IRCADb-01**</a> (3D Image Reconstruction for Comparison of Algorithm Database) <br>
10 women and 10 men with hepatic tumours in 75% of cases. <br>
***Keyboard:*** 3D CT scan, Cancer, Labeled, Segmentation <br>

- <a href="https://competitions.codalab.org/competitions/17094"> **LiTS**</a> (Liver Tumor Segmentation) <br>
***Keyboard:*** CT scan, Cancer, Labeled <br>
<a href="https://competitions.codalab.org/competitions/17094#results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/1901.04056"> ![paper](src/paper.png)</a>

- <a href="https://p2ilf.grand-challenge.org"> **P2ILF**</a> (Preoperative to Intraoperative Laparoscopy Fusion) <br>
***Keyboard:*** Laparoscopic video images, Segmentation, Registration  <br>
<a href="https://p2ilf.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://paip2019.grand-challenge.org"> **PAIP2019**</a> <br>
***Keyboard:*** Whole-slide images (WSIs), Cancer, Segmentation, Labeled, Hepatocellular Carcinoma (HCC) <br>
<a href="https://paip2019.grand-challenge.org/Leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://sliver07.grand-challenge.org"> **SLIVER07**</a> (Segmentation of the Liver Competition 2007) <br>
***Keyboard:*** 3D CT scan <br>
<a href="https://sliver07.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/4781564?isnumber=5175685&arnumber=4781564&count=18&index=11"> ![paper](src/paper.png)</a>

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=6885436"> **TCGA-LIHC**</a> (The Cancer Genome Atlas Liver Hepatocellular Carcinoma) <br>
It has used in <a href='https://zenodo.org/records/8179129'> LiverHccSeg </a> <br>
***Keyboard:*** MRI, Cancer <br>



### Lungs

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=21267414"> **4D Lung**</a> <br>
The images include four-dimensional (4D) fan beam (4D-FBCT) and 4D cone beam CT (4D-CBCT)
***Keyboard:*** Cancer <br>
<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3647023"> ![paper](src/paper.png) The dataset is described</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/22391105"> ![paper](src/paper.png)</a> 

- <a href="https://acdc-lunghp.grand-challenge.org/"> **ACDC-LungHP**</a> (Automatic Cancer Detection and Classification in Lung Histopathology) <br>
***Keyboard:*** Cancer, H&E staining, Pathology  <br>
<a href="https://acdc-lunghp.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/9265237"> ![paper](src/paper.png)</a> | <a href="http://arxiv.org/abs/1803.05471"> ![paper](src/paper.png)</a> 

- <a href="https://anode09.grand-challenge.org/"> **ANODE09**</a> (Automatic Nodule Detection 2009) <br>
Automatic detection of pulmonary nodules in chest <br>
***Keyboard:*** CT-scan <br>
<a href="https://anode09.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841510000587"> ![paper](src/paper.png)</a> 

- <a href="https://atm22.grand-challenge.org"> **ATM22**</a> (Airway Tree Modeling) <br>
Dataset provides CT scans with detailed pulmonary airway annotation.
***Keyboard:*** CT-scan, Labeled<br>
<a href="https://atm22.grand-challenge.org/evaluation/validation-phase-1-live-leaderboard/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841523002177"> ![paper](src/paper.png)</a>

- <a href="https://cxr-covid19.grand-challenge.org"> **Chest XR COVID-19 detection**</a> <br>
The dataset contains 20,000+ images and 3 classes: COVID-19, Pneumonia and Normal (healthy). <br>
***Keyboard:*** X-ray, Labeled <br>

- <a href="https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community"> **ChestX-ray8**</a> (ChestXray-NIHCC) <br>
100,000 anonymized chest x-ray images <br>
***Keyboard:*** X-ray, Labeled <br>
<a href="https://arxiv.org/abs/1705.02315"> ![paper](src/paper.png)</a> 

- <a href="https://stanfordmlgroup.github.io/competitions/chexpert/"> **CheXpert**</a> <br>
A Large Chest X-Ray Dataset. <br>
***Keyboard:*** X-ray, Labeled <br>
<a href="https://arxiv.org/abs/1901.07031"> ![paper](src/paper.png)</a>

- <a href="https://covid-segmentation.grand-challenge.org"> **COVID-19-20**</a> <br>
COVID-19 Lung CT Lesion Segmentation <br>
***Keyboard:*** CT scan, Labeled <br>
<a href="https://covid-segmentation.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/pii/S1361841522002353"> ![paper](src/paper.png)</a>

- <a href="https://data.uni-hannover.de/dataset/cov-19-img"> **COVID-19 Image Repository**</a> <br>
An anonymized data set of COVID-19 cases with a focus on radiological imaging <br>

- <a href="https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database"> **COVID-19 Radiography Database**</a> <br>
3616 COVID-19 Chest X-ray images and lung masks <br>
<a href="https://www.sciencedirect.com/science/article/pii/S001048252100113X"> ![paper](src/paper.png)</a> | <a href="https://ieeexplore.ieee.org/document/9144185"> ![paper](src/paper.png)</a>

- <a href="https://github.com/ieee8023/covid-chestxray-dataset"> **COVID-ChestXRay**</a> <br>
An database of COVID-19 cases with chest X-ray or CT images <br>
***Keyboard:*** CT scan, X-ray <br>
<a href="https://arxiv.org/abs/2006.11988"> ![paper](src/paper.png)</a> | <a href="https://arxiv.org/abs/2004.05405"> ![paper](src/paper.png)</a>

- <a href="https://github.com/UCSD-AI4H/COVID-CT"> **COVID-CT**</a> <br>
It contains 349 COVID-19 CT images from 216 patients and 463 non-COVID-19 CTs<br>
***Keyboard:*** CT scan, Classification <br>
<a href="https://covid-ct.grand-challenge.org/Leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2003.13865"> ![paper](src/paper.png)</a> 

- <a href="https://github.com/lindawangg/COVID-Net/blob/master/docs/COVIDx.md"> **COVIDx**</a> <br>
It is a collection of 8 datasets <br>
***Keyboard:*** CT scan, X-ray <br>
<a href="https://arxiv.org/abs/2003.09871"> ![paper](src/paper.png)</a>

- <a href="https://crass.grand-challenge.org"> **CRASS12**</a> (Chest Radiograph Anatomical Structure Segmentation) <br>
Automatic segmentation of anatomical structures in chest radiographs <br>
<a href="https://www.diagnijmegen.nl/publications/hoge12/?bibkey=Hoge12"> ![paper](src/paper.png)</a> 

- <a href="https://empire10.grand-challenge.org"> **EMPIRE10**</a> (Evaluation of Methods for Pulmonary Image Registration 2010) <br>
***Keyboard:*** CT, Registration of thoracic <br>
<a href="https://pubmed.ncbi.nlm.nih.gov/21632295"> ![paper](src/paper.png)</a> 

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=1966254"> **LIDC-IDRI**</a> (Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI)) <br>
***Keyboard:*** CT scan, Cancer, Labeled <br>
<a href="https://aapm.onlinelibrary.wiley.com/doi/10.1118/1.3528204"> ![paper](src/paper.png)</a> 

- <a href="https://lndb.grand-challenge.org"> **LNDb**</a> (Lung Nodule Database) <br>
Lung nodule detection, segmentation and characterization as well as prediction of patient follow-up <br>
***Keyboard:*** Cancer, CT-scan <br>
<a href="https://lndb.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/33740739"> ![paper](src/paper.png) </a> 

- <a href="https://lola11.grand-challenge.org/"> **LOLA11**</a> (LObe and Lung Analysis 2011) <br>
Compare methods for (semi-)automatic segmentation of the lungs and lobes from chest <br>
***Keyboard:*** segmentation, CT-scan <br>
<a href="https://lola11.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://lumic.grand-challenge.org"> **LUMIC**</a> <br>
***Keyboard:*** CT-scan, registration, Labeled<br>
<a href="https://pubmed.ncbi.nlm.nih.gov/30888690"> ![paper](src/paper.png)</a> 

- <a href="https://luna16.grand-challenge.org"> **LUNA16**</a> (LUng Nodule Analysis 2016) <br>
Nodule location detection <br>
***Keyboard:*** Cancer, CT-scan <br>
<a href="https://luna16.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841517301020"> ![paper](src/paper.png) Overview paper</a> 

- <a href="https://mela.grand-challenge.org"> **MELA**</a> (Mediastinal Lesion Analysis) <br>
Detectition mediastinal lesions from 1100 CT scans, consisting of 770 CTs for training, 110 CTs for validation, and 220 CTs for testing. <br>
***Keyboard:*** CT Scan <br>
<a href="https://mela.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://mela.grand-challenge.org"> **NSCLC-Radiomics**</a> (Non-Small Cell Lung Cancer) <br>
This collection contains images from 422 patients.  <br>
***Keyboard:*** CT Scan, Labeled <br>

- <a href="https://www.cancerimagingarchive.net/analysis-result/qin-lungct-seg"> **QIN Lung CT**</a> <br>
***Keyboard:*** Nodule, CT Scan, Segmentation <br>

- <a href="https://stoic2021.grand-challenge.org"> **STOIC2021**</a> <br>
Study of Thoracic CT in COVID-19 <br>
***Keyboard:*** CT scan <br>
<a href="https://stoic2021.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubs.rsna.org/doi/10.1148/radiol.2021210384"> ![paper](src/paper.png)</a>

- <a href="https://vessel12.grand-challenge.org/"> **VESSEL12**</a> (VESsel SEgmentation in the Lung 2012) <br>
Automatic (and semi-automatic) segmentation of blood vessels in the lungs from CT images <br>
***Keyboard:*** CT-scan <br>
<a href="https://vessel12.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S136184151400111X"> ![paper](src/paper.png) Overview paper</a> 




______

## Musculoskeletal System

### Bones

- <a href="https://stanfordmlgroup.github.io/competitions/mura"> **MURA**</a> (MUsculoskeletal RAdiographs) <br>
Large Dataset for Abnormality Detection in Musculoskeletal Radiographs <br>
***Keyboard:*** X-ray, Labeled<br>
<a href="https://arxiv.org/abs/1712.06957"> ![paper](src/paper.png)</a> 

- <a href="https://ribfrac.grand-challenge.org"> **RibFrac**</a> <br> 
A dataset for detect and classify around 5,000 rib fractures from 660 computed tomography (CT) scans <br>
***Keyboard:*** CT scan, Labeled <br>
<a href="https://ribfrac.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://spider.grand-challenge.org"> **SPIDER**</a> (SPIne Segmentation: Discs, vERtebrae, and spinal canal)<br>
A lumbar spine MR dataset with reference segmentations of vertebrae, intervertebral discs (IVDs), and spinal canal <br>
***Keyboard:*** MRI <br>
<a href="https://spider.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2306.12217"> ![paper](src/paper.png)</a>

- <a href="http://spineweb.digitalimaginggroup.ca"> **SpineWeb**</a> <br>
16 spinal imaging datasets

- <a href="https://github.com/anjany/verse"> **VerSe**</a> <br> Large Scale Vertebrae Segmentation <br>
***Keyboard:*** CT scan, Segmentation <br>
<a href="https://verse2019.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841521002127"> ![paper](src/paper.png)</a> | <a href="https://pubs.rsna.org/doi/10.1148/ryai.2020190138"> ![paper](src/paper.png)</a>


### Joints

- <a href="https://k2s.grand-challenge.org"> **K2S**</a> <br>
A dataset of high-resolution 3D knee MRI including raw k-space data and post-processing annotations with masks for tissue segmentation. <br>
***Keyboard:*** MRI, Labeled<br>

- <a href="https://knoap2020.grand-challenge.org"> **KNOAP2020**</a> (KNee OsteoArthritis Prediction) <br>
***Keyboard:*** MRI scans, X-ray, Labeled<br>
<a href="https://www.oarsijournal.com/article/S1063-4584(22)00864-0/fulltext"> ![paper](src/paper.png)</a> 

- <a href="https://stanfordmlgroup.github.io/competitions/mrnet"> **MRNet**</a> <br>
Diagnosis of abnormalities from Knee MRs <br>
***Keyboard:*** MRI, Labeled<br>
<a href="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002699"> ![paper](src/paper.png)</a> 

<!---
### Muscles
-->

_______

## Pelvis and Reproductive Organs

### Female Reproductive Organs

- <a href="https://github.com/cwwang1979/MICCAI_ATEC23challenge"> **ATEC23**</a> <br>
Automated prediction of treatment effectiveness in ovarian cancer using histopathological images <br>
***Keyboard:*** Whole Slide Images (WSIs), Cancer <br>
<a href="https://arxiv.org/abs/2310.12866"> ![paper](src/paper.png)</a>

- <a href="https://a-afma.grand-challenge.org"> **A-AFMA**</a> (Automatic amniotic fluid measurement and analysis) <br>
The goal is measurement of the maximum vertical pocket (MVP) <br>
***Keyboard:*** Ultrasound Video Clip <br>

- <a href="https://zenodo.org/records/7372187"> **ENDO-AID**</a> <br>
The dataset consists of 91 digital pathology whole-slide images (WSI) of endometrium carcinoma Pipelle biopsies, stained with hematoxylin and eosin (H&E). <br>
***Keyboard:*** Whole-slide images (WSI), Cancer <br>

- <a href="https://hc18.grand-challenge.org"> **HC18**</a> <br>
Measurement of fetal head circumference (HC)<br>
***Keyboard:*** Ultrasound imaging, Labeled <br>
<a href="https://hc18.grand-challenge.org/evaluation/challenge/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://figshare.com/articles/dataset/JNU-IFM/14371652"> **JNU-IFM**</a> <br>
An intrapartum transperineal ultrasound dataset of the Intelligent Fetal Monitoring <br>
***Keyboard:*** Ultrasound videos, Labeled <br>
<a href="https://www.sciencedirect.com/science/article/pii/S2352340922001160"> ![paper](src/paper.png)</a>

- <a href="https://ps-fh-aop-2023.grand-challenge.org"> **Ps-Fh-Aop-2023**</a> (Pubic Symphysis-Fetal Head Segmentation and Angle of Progression) <br>
***Keyboard:*** Ultrasound imaging, Labeled <br>
<a href="https://ps-fh-aop-2023.grand-challenge.org/evaluation/phase-two/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>


### Male Reproductive Organs

- <a href="https://aggc22.grand-challenge.org">**AGGC22**</a> (Automated Gleason Grading Challenge 2022) <br>
Dataset of prostatectomy and biopsy specimens with annotations  <br>
***Keyboard:*** H&E-stained whole slide image <br>
<a href="https://aggc22.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.researchgate.net/publication/363780482_Comprehensive_AI_Model_Development_for_Gleason_Grading_From_Scanning_Cloud-based_Annotation_to_Pathologist-AI_Interaction"> ![paper](src/paper.png)</a>

- <a href="https://auto-rtp.grand-challenge.org">**AUTO-RTP**</a> (Fully Automated Radiotherapy Treatment Planning) <br>
***Keyboard:*** Cancer<br>
<a href="https://auto-rtp.grand-challenge.org/evaluation/data-format-confirmation/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://gleason2019.grand-challenge.org"> **Gleason 2019**</a> <br>
Gleason grading of prostate cancer in digital histopathology images <br>
***Keyboard:*** H&E-stained histopathology image, Cancer, Labeled <br>
<a href="https://gleason2019.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://www.kaggle.com/c/prostate-cancer-grade-assessment"> **PANDA**</a> (Prostate cANcer graDe Assessment) <br>
Classifying the severity of prostate cancer from microscopy scans of prostate biopsy samples <br>
***Keyboard:*** whole-slide images (WSI), Cancer <br>
<a href="https://www.nature.com/articles/s41591-021-01620-2"> ![paper](src/paper.png)</a>

- <a href="https://pi-cai.grand-challenge.org/"> **PI-CAI**</a> (Prostate Imaging: Cancer AI) <br>
***Keyboard:*** Prostate, MRI, Cancer, Labeled <br>
<a href="https://pi-cai.grand-challenge.org/evaluation/open-development-phase/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://promise12.grand-challenge.org"> **PROMISE12**</a> (Prostate MR Image Segmentation 2012) <br>
Compare interactive and (semi)-automatic segmentation algorithms for MRI of the prostate <br>
***Keyboard:*** T2-weighted MRI, Labeled <br>
<a href="https://promise12.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841513001734"> ![paper](src/paper.png) Overview paper</a>


______
## Other Organs and Systems

### Lymph Nodes

- <a href="https://camelyon16.grand-challenge.org"> **CAMELYON16**</a> <br>
Detection of metastases in hematoxylin and eosin (H&E) stained whole-slide images of lymph node sections <br>
***Keyboard:*** Cancer, Digital pathology, Lymph node detection <br>
<a href="https://camelyon16.grand-challenge.org/Results"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://jamanetwork.com/journals/jama/article-abstract/2665774"> ![paper](src/paper.png)</a> | <a href="https://academic.oup.com/gigascience/article/7/6/giy065/5026175"> ![paper](src/paper.png)</a>

- <a href="https://camelyon17.grand-challenge.org"> **CAMELYON17**</a> <br>
Evaluate new and existing algorithms for automated detection and classification of breast cancer metastases in whole-slide images of histological lymph node sections <br>
***Keyboard:*** Cancer, Digital pathology, Lymph node detection <br>
<a href="https://camelyon17.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://ieeexplore.ieee.org/document/8447230"> ![paper](src/paper.png)</a> | <a href="https://academic.oup.com/gigascience/article/7/6/giy065/5026175"> ![paper](src/paper.png)</a>

- <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=19726546"> **CT Lymph nodes**</a> <br>
90 CTs dataset of lymph nodes <br>
***Keyboard:*** CT scan, Lymph node detection

- <a href="https://lnq2023.grand-challenge.org"> **LNQ2023**</a> (Mediastinal Lymph Node Quantification) <br>
Segmentation of Heterogeneous CT Data <br>
***Keyboard:*** CT scan, Cancer  <br>
<a href="https://lnq2023.grand-challenge.org/evaluation/validation/leaderboard/"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://huggingface.co/datasets/andreped/LyNoS"> **LyNoS**</a>  <br>
15 CTs with corresponding lymph nodes, azygos, esophagus, and subclavian carotid arteries  <br>
***Keyboard:*** CT scan, Segmentation <br>
<a href="https://www.tandfonline.com/doi/full/10.1080/21681163.2022.2043778"> ![paper](src/paper.png)</a>

- <a href="https://github.com/basveeling/pcam"> **PatchCamelyon**</a> <br>
Image classification dataset consists of 327.680 color images extracted from histopathologic scans of lymph node sections. <br>
***Keyboard:*** Labeled <br>
<a href="https://patchcamelyon.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/1806.03962"> ![paper](src/paper.png)</a>


______
## Multi Organs Datasets

- <a href="https://zenodo.org/records/7155725#.Y0OOCOxBztM"> **AMOS**</a> <br>
A large-scale abdominal multi-organ benchmark for versatile medical image segmentation <br>
***Keyboard:***  Multi-tissue (15 abdominal organs), MRI, CT scan<br>
<a href="https://amos22.grand-challenge.org/evaluation/amos-ct-regular-evaluation/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions"> **AutoPET**</a><br>
A whole-body FDG-PET/CT dataset with manually annotated tumor lesions (FDG-PET-CT-Lesions) <br>
***Keyboard:*** PET - CT scan, Labeled <br>

- <a href="https://chaos.grand-challenge.org"> **CHAOS**</a> (Combined (CT-MR) Healthy Abdominal Organ Segmentation) <br>
There are 20 training and 20 testing cases in the CT dataset. MRI dataset contains 20 training and 20 testing cases with T1-Dual and T2 SPIR sequences. <br>
***Keyboard:*** *Liver, Kidneys, Spleen*, CT Scan, MRI, Labeled <br>
<a href="https://chaos.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841520303145"> ![paper](src/paper.png)</a>

- <a href="https://ead2019.grand-challenge.org/"> **EAD 2019**</a> (Endoscopy artifact detection) <br>
Facilitating diagnosis and treatment of diseases in hollow organs. <br>
***Keyboard:***  Multi-tissue, Multi-modality, Video Endoscopy, Labeled <br>
<a href="https://ead2019.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/1905.03209"> ![paper](src/paper.png)</a>

- <a href="https://fastpet-ld.grand-challenge.org"> **fastPET-LD**</a> (Fast PET-CT lesion detection) <br>
***Keyboard:*** Hot spots, PET - CT scan, Labeled, Detection <br>
<a href="https://fastpet-ld.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://flare22.grand-challenge.org"> **FLARE 2022**</a> (Fast and Low-resource semi-supervised Abdominal oRgan sEgmentation) <br>
A small number of labeled cases (50) and a large number of unlabeled cases (2000) in the training set. <br>
***Keyboard:***  Multi-tissue (13 organs), CT scan, Labeled <br>
<a href="https://flare22.grand-challenge.org/evaluation/testing-dsc/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2308.05862"> ![paper](src/paper.png)</a>

- <a href="https://han-seg2023.grand-challenge.org"> **HaN-Seg**</a> (Head and Neck Segmentation) <br>
Images of 60 patients aged 34–79 years that were appointed for image-guided Radiotherapy in the HaN region <br>
***Keyboard:*** *30 organs-at-risk*, CT Scan, MRI, Labeled <br>
<a href="https://han-seg2023.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.16197"> ![paper](src/paper.png)</a>

- <a href="https://hecktor.grand-challenge.org"> **HECKTOR**</a> (HEad and neCK TumOR segmentation and outcome prediction) <br>
The data were collected for a total of 883 cases consisting of FDG-PET/CT images and clinical information. <br>
***Keyboard:*** *Head, Neck, Lymph nodes*, FDG-PET/CT images, Cancer, Labeled <br>
<a href="https://hecktor.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://pubmed.ncbi.nlm.nih.gov/37195050"> ![paper](src/paper.png) Overview paper</a>

- <a href="https://lyon19.grand-challenge.org"> **LYON19**</a> <br>
The test set contains Region of Interests (ROIs) selected from whole-slide images (WSI) of immunohistochemistry (IHC) stained specimens <br>
***Keyboard:*** *breast, colon, prostate*, whole-slide images (WSI) <br>
<a href="https://lyon19.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://www.sciencedirect.com/science/article/abs/pii/S1361841519300829"> ![paper](src/paper.png)</a>

- <a href="https://medshapenet.ikim.nrw"> **MedShapeNet**</a> <br>
This dataset contains over 100,000 3D medical shapes, including bones, organs, vessels, muscles, etc., as well as surgical instruments. It has used in <a href='https://autoimplant.grand-challenge.org'> AutoImplant </a> <br>
<a href="https://proj-page.github.io/medshapenet_publications.html"> ![paper](src/paper.png)</a>

- <a href="https://lunit-io.github.io/research/ocelot_dataset"> **OCELOT**</a> <br>
A dataset purposely dedicated to the study of cell-tissue relationships for cell detection in histopathology <br>
***Keyboard:*** *Kidney, Head-neck, Prostate, Stomach, Endometrium, and Bladder*, Whole-slide images (WSIs) <br>
<a href="https://ocelot2023.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2303.13110"> ![paper](src/paper.png)</a>

- <a href="https://paip2021.grand-challenge.org"> **PAIP2021**</a> <br>
Detection of Perineural Invasion in Multiple Organ Cancer <br>
***Keyboard:*** *Colon, Prostate and Pancreatobiliary tract*, Whole-slide images (WSIs), Cancer, Labeled <br>
<a href="https://paip2021.grand-challenge.org/evaluation/validation/leaderboard"> ![Leaderboard](src/leaderboard.png)</a>

- <a href="https://segrap2023.grand-challenge.org"> **SegRap2023**</a> <br>
A Benchmark of Organs-at-Risk and Gross Tumor Volume Segmentation for Radiotherapy Planning of Nasopharyngeal Carcinoma <br>
***Keyboard:*** *45 organs-at-risk*, CT Scan, Cancer <br>
<a href="https://segrap2023.grand-challenge.org/evaluation/challenge/leaderboard"> ![Leaderboard](src/leaderboard.png)</a> | <a href="https://arxiv.org/abs/2312.09576"> ![paper](src/paper.png)</a>

- <a href="https://structseg2019.grand-challenge.org"> **StructSeg2019**</a> <br>
Segmentation of organs-at-risk (OAR) and gross target volume (GTV) of tumors of two types of cancers, nasopharynx cancer and lung cancer, for radiation therapy planning. <br>
***Keyboard:*** *Head & neck, Lung*, CT scans, Cancer, Labeled <br>

- <a href="https://ultra-low-dose-pet.grand-challenge.org"> **Ultra-low Dose PET Imaging**</a> <br>
The dataset contains 1447 subjects of whole-body 18F-FDG PET imaging <br>
***Keyboard:*** Positron emission tomography (PET) <br>


__________________


