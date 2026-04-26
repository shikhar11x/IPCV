<p align="center">
  <img src="https://img.shields.io/badge/K.R.%20Mangalam-UNIVERSITY-blue?style=for-the-badge&logo=google-scholar&logoColor=white&labelColor=0A3D91&color=E53935">
</p>

# Image Processing & Computer Vision

**Course:** Image Processing & Computer Vision  
**Student:** Shikhar Bajpai &nbsp;|&nbsp; Roll No: 2301010188  
**Facult Name:** Atisha Dahiya Ma'am  

---

## Repository Structure

```
ipcv/
├── Assignment-1/          ← Smart Document Scanner
│   ├── scanner.py
│   ├── README.md
│   ├── images/
│   └── outputs/
│
├── Assignment-2/          ← Surveillance Image Restoration
│   ├── restoration.py
│   ├── README.md
│   ├── images/
│   └── outputs/
│
├── Assignment-3/          ← Medical Image Compression & Segmentation
│   ├── medical_image_system.py
│   ├── README.md
│   ├── images/
│   └── outputs/
│
├── Assignment-4/          ← Feature-Based Traffic Monitoring
│   ├── traffic_monitoring.py
│   ├── README.md
│   ├── images/
│   └── outputs/
│
└── Assignment-5/          ← Intelligent Image Enhancement & Analysis (Capstone)
    ├── main.py
    ├── README.md
    ├── images/
    └── outputs/
```

---

## Assignments Overview

### Assignment 1 — Smart Document Scanner & Quality Analysis
**Script:** `scanner.py` &nbsp;|&nbsp; **Weightage:** 5 Marks  

Simulates a real-world document digitization system. Analyzes how sampling (resolution reduction) and quantization (bit-depth reduction) affect document readability and OCR accuracy.

| Task | What it does |
|------|-------------|
| Task 1 | Project setup, header, welcome message |
| Task 2 | Load document image, resize to 512×512, grayscale conversion |
| Task 3 | Down-sample to 512×512 / 256×256 / 128×128, upscale back, compare sharpness |
| Task 4 | Quantize to 256 / 16 / 4 gray levels, visualize artifacts |
| Task 5 | Quality observations and analytical comparison |

**Images needed:** `images/doc1.jpg`, `images/doc2.jpg`, `images/doc3.jpg` (document scans / printed text)  
**Run:** `python scanner.py`

---

### Assignment 2 — Image Restoration for Surveillance Camera Systems
**Script:** `restoration.py` &nbsp;|&nbsp; **Weightage:** 5 Marks  

Simulates real-world surveillance noise (Gaussian, Salt-and-Pepper) and restores image quality using classical spatial filters. Evaluates restoration using MSE and PSNR.

| Task | What it does |
|------|-------------|
| Task 1 | Load surveillance-style image, grayscale conversion |
| Task 2 | Add Gaussian noise + Salt-and-Pepper noise |
| Task 3 | Apply Mean / Median / Gaussian filters |
| Task 4 | Compute MSE and PSNR for each filter |
| Task 5 | Filter-wise performance comparison and best method identification |

**Images needed:** `images/surv1.jpg`, `images/surv2.jpg`, `images/surv3.jpg` (street, corridor, parking)  
**Run:** `python restoration.py`

---

### Assignment 3 — Medical Image Compression & Segmentation System
**Script:** `medical_image_system.py` &nbsp;|&nbsp; **Weightage:** 5 Marks  

Focuses on compressing medical images using Run Length Encoding and segmenting regions of interest (tumors, bones, organs) using thresholding and morphological operations.

| Task | What it does |
|------|-------------|
| Task 1 | Load X-ray/MRI/CT image, implement RLE, compute compression ratio |
| Task 2 | Global thresholding + Otsu's thresholding, identify ROIs |
| Task 3 | Dilation + Erosion to refine segmented regions |
| Task 4 | Compare segmentation results, discuss clinical relevance |

**Images needed:** `images/xray.jpg`, `images/mri.jpg`, `images/ct.jpg` (medical images from public datasets)  
**Run:** `python medical_image_system.py`

---

### Assignment 4 — Feature-Based Traffic Monitoring System
**Script:** `traffic_monitoring.py` &nbsp;|&nbsp; **Weightage:** 5 Marks  

Simulates a feature-based traffic analysis system that detects edges, represents objects using contours and bounding boxes, and extracts keypoint features using ORB.

| Task | What it does |
|------|-------------|
| Task 1 | Sobel edge detection + Canny edge detection, compare quality |
| Task 2 | Contour detection, bounding boxes, object area & perimeter |
| Task 3 | ORB keypoint extraction and descriptor visualization |
| Task 4 | Comparative analysis of edge detectors + traffic monitoring relevance |

**Images needed:** `images/traffic1.jpg`, `images/traffic2.jpg`, `images/traffic3.jpg` (road intersection, highway, pedestrian crossing)  
**Run:** `python traffic_monitoring.py`

---

### Assignment 5 — Intelligent Image Enhancement & Analysis System (Capstone)
**Script:** `main.py` &nbsp;|&nbsp; **Weightage:** 10 Marks  

End-to-end capstone project integrating all units — acquisition, enhancement, restoration, segmentation, feature extraction, and performance evaluation into a single pipeline.

| Task | What it does |
|------|-------------|
| Task 1 | Project setup, header comments, welcome banner |
| Task 2 | Image acquisition, resize to 512×512, grayscale conversion |
| Task 3 | Gaussian & S&P noise + Mean / Median / Gaussian filtering + CLAHE |
| Task 4 | Global & Otsu thresholding + Dilation & Erosion |
| Task 5 | Sobel & Canny edges + Contours + Bounding boxes + ORB keypoints |
| Task 6 | MSE, PSNR, SSIM — Original vs Enhanced & Restored |
| Task 7 | Full pipeline visualization + conclusion |

**Images needed:** `images/input1.jpg`, `images/input2.jpg`, `images/input3.jpg` (any 3 different photos)  
**Run:** `python main.py images/input1.jpg`

---

## Installation

All assignments use the same dependencies:

```bash
pip install opencv-python numpy matplotlib scikit-image
```

---

## Output Files

Each assignment auto-creates an `outputs/` folder with all result images saved as `.png` files. No manual setup needed — just run the script.

---

## References

- [OpenCV Documentation](https://docs.opencv.org)
- [scikit-image Documentation](https://scikit-image.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- Gonzalez & Woods — *Digital Image Processing*, 4th Ed.
- Rublee et al. (2011) — *ORB: An efficient alternative to SIFT or SURF*, ICCV

---

## Academic Integrity

All submissions are original individual work by Shikhar Bajpai (2301010188).  
External references are cited above. No plagiarism has been done.
