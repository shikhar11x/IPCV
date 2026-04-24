# 📄 Smart Document Scanner & Quality Analysis System

## 🧠 Course Details

* **Course:** Image Processing & Computer Vision
* **Assignment:** Mini Project Assignment (Assignment-1)
* **Student Name:** Shikhar Bajpai
* **Roll No:** 2301010188
* **University:** KR Mangalam University

---

## 📌 Problem Statement

In real-world environments such as universities, banks, and offices, documents are often digitized using scanners or mobile cameras. However, poor image acquisition, low resolution, and reduced bit-depth can significantly affect readability and OCR (Optical Character Recognition) accuracy.

This project simulates a Smart Document Scanner System to analyze how:

* Image Sampling (Resolution)
* Image Quantization (Bit Depth)

affect document quality.

---

## 🎯 Objectives

* Understand image acquisition and preprocessing
* Convert images to grayscale
* Analyze resolution (sampling effects)
* Analyze bit-depth reduction (quantization)
* Compare visual quality and readability
* Evaluate suitability for OCR systems

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib

---

## 📂 Project Structure

Assignment-1/
│── scanner.py
│── README.md
│── inputs/
│   └── doc1.png
│── outputs/
│   ├── result.png
│   └── terminalResult.png

---

## ⚙️ Features Implemented

### ✅ Image Acquisition

* Input image loaded from inputs/ folder
* Resized to 512×512
* Converted to grayscale

### ✅ Image Sampling (Resolution Analysis)

* High Resolution → 512×512
* Medium Resolution → 256×256
* Low Resolution → 128×128
* Upscaled for comparison

### ✅ Image Quantization (Gray Level Reduction)

* 8-bit (256 levels) → Original quality
* 4-bit (16 levels) → Slight distortion
* 2-bit (4 levels) → Heavy distortion

### ✅ Visualization

* All outputs displayed in a single comparison figure
* Results saved in outputs/ folder

---

## 📊 Output Results

### 🔹 Input Image

* IPCV/Assignment-1/inputs/doc1.png

### 🔹 Output Images

* outputs/result.png
* outputs/terminalResult.png

---

## 📈 Observations & Analysis

### 🔍 Resolution (Sampling Effects)

* High resolution preserves text clarity and sharp edges
* Medium resolution introduces slight blur in smaller text
* Low resolution results in loss of fine details and readability

### 🎨 Quantization Effects

* 8-bit images maintain smooth grayscale transitions
* 4-bit images show visible banding and reduced detail
* 2-bit images appear blocky with major information loss

### 🤖 OCR Suitability

* OCR performs best on:

  * High resolution images
  * Higher bit-depth (8-bit)
* Poor resolution and low bit-depth significantly reduce OCR accuracy

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

pip install opencv-python numpy matplotlib

### Step 2: Run the Script

python scanner.py

### Step 3: Provide Input

Enter image name: doc1.png

---

## 🧪 Sample Runs

This project can be tested using:

* Printed document images
* Scanned PDF pages
* Mobile captured documents

---

## 📎 References

* OpenCV Official Documentation
* Digital Image Processing Concepts (Sampling & Quantization)
* Python Matplotlib Docs

---

## ⚠️ Academic Integrity

This project is an original submission. Any external references used are properly cited. No plagiarism has been done.

---

## 🚀 Conclusion

This project successfully demonstrates how image quality is affected by resolution and bit-depth. It highlights the importance of proper image acquisition for document scanning and OCR-based systems.

---

✨ Thank you!
