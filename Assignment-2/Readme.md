# 📷 Image Restoration for Surveillance Camera Systems

## 🧠 Course Details

* **Course:** Image Processing & Computer Vision  
* **Assignment:** Mini Project Assignment (Assignment-2)  
* **Student Name:** Shikhar Bajpai  
* **Roll No:** 2301010188  
* **University:** KR Mangalam University  

---

## 📌 Problem Statement

Surveillance cameras often operate in challenging environments such as low light, rain, fog, and dust. These conditions introduce noise into captured images, making it difficult to identify objects clearly.

This project simulates real-world noise conditions and restores image quality using image processing techniques.

---

## 🎯 Objectives

* Understand image noise types  
* Simulate real-world noise (Gaussian, Salt & Pepper)  
* Apply image restoration filters  
* Evaluate performance using MSE and PSNR  

---

## 🛠️ Technologies Used

* Python  
* OpenCV  
* NumPy  
* Matplotlib  

---

## 📂 Project Structure


Assignment-2/
│── main.py
│── Readme.md
│
├── inputs/
│ └── doc1.jpg
│
└── outputs/
├── original.png
├── gaussian_noise.png
├── sp_noise.png
├── mean_gaussian.png
├── median_gaussian.png
├── gaussian_filtered.png
├── mean_sp.png
├── median_sp.png
├── gaussian_sp.png
└── restoration_result.png


---

## ⚙️ Features Implemented

### ✅ Image Preprocessing
* Input image loaded from inputs folder  
* Resized to 512×512  
* Converted to grayscale  

### ✅ Noise Modeling
* Gaussian Noise (sensor noise simulation)  
* Salt & Pepper Noise (impulse noise simulation)  

### ✅ Image Restoration
Applied filters:
* Mean Filter  
* Median Filter  
* Gaussian Filter  

### ✅ Performance Evaluation
* Mean Squared Error (MSE)  
* Peak Signal-to-Noise Ratio (PSNR)  

---

## 📊 Output Results

### 🔹 Original Image
![Original](inputs/doc1.jpg)

### 🔹 Noisy Images
**Gaussian Noise**
![Gaussian Noise](outputs/gaussian_noise.png)

**Salt & Pepper Noise**
![SP Noise](outputs/sp_noise.png)

---

### 🔹 Restored Images

#### Gaussian Noise Restoration
![Mean Gaussian](outputs/mean_gaussian.png)  
![Median Gaussian](outputs/median_gaussian.png)  
![Gaussian Filter](outputs/gaussian_filtered.png)  

#### Salt & Pepper Restoration
![Mean SP](outputs/mean_sp.png)  
![Median SP](outputs/median_sp.png)  
![Gaussian SP](outputs/gaussian_sp.png)  

---

### 🔹 Final Comparison
![Comparison](outputs/restoration_result.png)

![Terminal Result](outputs/terminalResult.png)

---

## 📈 Observations & Analysis

### 🔍 Gaussian Noise
* Mean and Gaussian filters perform better  
* Median filter is less effective  

### 🔍 Salt & Pepper Noise
* Median filter gives best results  
* Preserves edges and removes noise effectively  

### 📊 Performance Insight
* Lower MSE = Better quality  
* Higher PSNR = Better restoration  

---

## ▶️ How to Run

### Step 1: Install Dependencies

pip install opencv-python numpy matplotlib


### Step 2: Run the Code

python main.py


---

## 🧪 Sample Inputs

You can test using:
* Street view images  
* Parking lot images  
* Corridor images  

---

## 📎 References
* OpenCV Documentation  
* Digital Image Processing Concepts  
* Python Libraries Documentation  

---

## ⚠️ Academic Integrity

This project is an original submission. No plagiarism has been done.

---

## 🚀 Conclusion

This project demonstrates how different noise types affect images and how appropriate filtering techniques can restore image quality. The results highlight that selecting the right filter depends on the type of noise present.

---

✨ Thank you!
