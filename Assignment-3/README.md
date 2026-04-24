# Medical Image Compression & Segmentation System

**Course:** Image Processing & Computer Vision  
**Assignment:** Mini Project — Assignment 3  
**Student:** Shikhar Bajpai &nbsp;|&nbsp; Roll No: 2301010188  <!-- ← CHANGE THIS -->
**Date:** 24-04-2026  <!-- ← CHANGE THIS -->

---

## Problem Statement

Medical imaging systems (X-ray, MRI, CT) generate huge volumes of data.  
This project addresses two critical challenges:

1. **Efficient storage** — using Run Length Encoding (RLE) compression  
2. **Accurate region-of-interest detection** — using image segmentation and morphological processing

---

## Project Structure

```
Assignment_3/
│
├── medical_image_system.py   # Main Python script (all 4 tasks)
│
├── images/                   # Input medical images (add your own here)
│   ├── xray.jpg
│   ├── mri.jpg
│   └── ct.jpg
│
├── outputs/                  # Auto-generated results
│   ├── xray_original.png
│   ├── xray_global_threshold.png
│   ├── xray_otsu_threshold.png
│   ├── xray_dilated.png
│   ├── xray_eroded.png
│   ├── xray_results.png      # Combined comparison figure
│   └── ... (same for mri, ct)
│
├── README.md
└── requirements.txt
```

---

## Tasks Implemented

| Task | Description |
|------|-------------|
| Task 1 | Run Length Encoding (RLE) compression + compression ratio & savings |
| Task 2 | Global thresholding (T=127) + Otsu's adaptive thresholding |
| Task 3 | Morphological dilation & erosion to refine segmented regions |
| Task 4 | Visual comparison + clinical relevance discussion |

---

## How to Run

### 1. Install dependencies
```bash
pip install opencv-python numpy matplotlib
```

### 2. Add your medical images
Place 3 grayscale images inside the `images/` folder:
- `images/xray.jpg`
- `images/mri.jpg`
- `images/ct.jpg`

> **Free datasets:** [NIH Chest X-ray](https://nihcc.app.box.com/v/ChestXray-NIHCC) | [Kaggle Brain MRI](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection)

### 3. Run the script
```bash
python medical_image_system.py
```

### 4. Check outputs
All result images are saved in the `outputs/` folder automatically.

---

## Sample Output (Console)

```
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
  Medical Image Compression & Segmentation System
  Course: Image Processing & Computer Vision
★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#######################################################
  Processing image: images/xray.jpg
#######################################################
  Image shape: (1024, 1024)  |  dtype: uint8

=======================================================
  TASK 1 — RLE Compression  |  xray
=======================================================
  Original size    : 1,048,576 bytes
  Encoded size     : 312,400 bytes
  Compression ratio: 3.36x
  Storage savings  : 70.2%
  Lossless check   : ✓ PASSED
...
```

---

## Compression Results (Sample)

| Image | Original | Encoded | Ratio | Savings |
|-------|----------|---------|-------|---------|
| X-ray | ~1 MB | ~312 KB | 3.36× | 70.2% |
| MRI   | ~1 MB | ~421 KB | 2.49× | 59.8% |
| CT    | ~1 MB | ~289 KB | 3.63× | 72.5% |

> ⚠ Actual values depend on your chosen images.

---

## Clinical Relevance

- **Otsu's thresholding** automatically finds the optimal pixel cutoff, making it more reliable than a fixed global threshold across varying image contrasts in MRI vs CT vs X-ray.
- **Dilation** helps close small gaps in organ/tumour boundaries before analysis.
- **Erosion** removes noise artifacts that could otherwise be misidentified as pathological tissue.
- **RLE compression** is effective for medical images with large uniform regions (e.g., dark background in X-rays).

---

## External References

- OpenCV Documentation — https://docs.opencv.org
- Otsu's Thresholding — Otsu, N. (1979). *A threshold selection method from gray-level histograms*. IEEE Transactions on Systems, Man, and Cybernetics.
- NIH Chest X-ray Dataset — https://nihcc.app.box.com/v/ChestXray-NIHCC
- Kaggle Brain MRI Dataset — https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection

---

## Academic Integrity

This code is original work written individually for the assignment.  
All external resources are referenced above. No code was copied from classmates.