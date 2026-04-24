"""
Name: Shikhar Bajpai
Roll No: 2301010188
Course: Image Processing & Computer Vision
Unit: 1
Assignment Title: Smart Document Scanner & Quality Analysis System
Date: 12-Feb-2026
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print("📄 Welcome to Smart Document Scanner & Quality Analysis System")
print("This system analyzes how resolution and bit-depth affect document quality.\n")

# Create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -----------------------------
# Function: Quantization
# -----------------------------
def quantize_image(img, levels):
    factor = 256 // levels
    quantized = (img // factor) * factor
    return quantized

# -----------------------------
# Function: Sampling
# -----------------------------
def sample_image(img, size):
    down = cv2.resize(img, size)
    up = cv2.resize(down, (512, 512))
    return up

# -----------------------------
# Load Image
# -----------------------------
image_path = 'inputs/doc1.png'

img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found!")
    exit()

# Resize to standard size
img = cv2.resize(img, (512, 512))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Sampling
# -----------------------------
high_res = gray
medium_res = sample_image(gray, (256, 256))
low_res = sample_image(gray, (128, 128))

# -----------------------------
# Quantization
# -----------------------------
q_256 = gray  # 8-bit
q_16 = quantize_image(gray, 16)
q_4 = quantize_image(gray, 4)

# -----------------------------
# Plot Results
# -----------------------------
titles = [
    "Original", "Grayscale",
    "512x512", "256x256", "128x128",
    "8-bit", "4-bit", "2-bit"
]

images = [
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gray,
    high_res, medium_res, low_res,
    q_256, q_16, q_4
]

plt.figure(figsize=(12, 8))

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

# Save output
output_path = "outputs/result.png"
plt.savefig(output_path)
plt.show()

print(f"\n✅ Output saved at {output_path}")

# -----------------------------
# Observations
# -----------------------------
print("\n📊 Observations:")
print("1. High resolution (512x512) preserves text clarity.")
print("2. Medium resolution shows slight blur in small text.")
print("3. Low resolution causes loss of fine details.")
print("4. 8-bit image gives smooth grayscale transitions.")
print("5. 4-bit introduces visible banding.")
print("6. 2-bit heavily distorts text and reduces readability.")
print("7. OCR works best on high resolution + high bit-depth images.")