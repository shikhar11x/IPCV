"""
Name: Shikhar Bajpai
Roll No: 2301010188
Course: Image Processing & Computer Vision
Unit: 1
Assignment Title: Image Restoration for Surveillance Camera Systems
Date: 14-Feb-2026
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print("📷 Image Restoration for Surveillance Systems")
print("Simulating noise and applying filters...\n")

# -----------------------------
# Auto Path (NO INPUT NEEDED)
# -----------------------------
image_path = "inputs/doc1.jpg"

# Create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -----------------------------
# Load Image
# -----------------------------
img = cv2.imread(image_path)

if img is None:
    print("❌ Image not found at:", image_path)
    exit()

# Resize
img = cv2.resize(img, (512, 512))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Noise Functions
# -----------------------------
def add_gaussian_noise(image):
    mean = 0
    sigma = 25
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy = image + gaussian
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(image):
    noisy = image.copy()
    prob = 0.02

    # Salt
    num_salt = int(prob * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy[coords[0], coords[1]] = 255

    # Pepper
    num_pepper = int(prob * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy

# -----------------------------
# Add Noise
# -----------------------------
gaussian_noise = add_gaussian_noise(gray)
sp_noise = add_salt_pepper_noise(gray)

# -----------------------------
# Filters
# -----------------------------
# Mean Filter
mean_gaussian = cv2.blur(gaussian_noise, (3, 3))
mean_sp = cv2.blur(sp_noise, (3, 3))

# Median Filter
median_gaussian = cv2.medianBlur(gaussian_noise, 3)
median_sp = cv2.medianBlur(sp_noise, 3)

# Gaussian Filter
gauss_gaussian = cv2.GaussianBlur(gaussian_noise, (3, 3), 0)
gauss_sp = cv2.GaussianBlur(sp_noise, (3, 3), 0)

# -----------------------------
# Metrics
# -----------------------------
def mse(original, restored):
    return np.mean((original - restored) ** 2)

def psnr(original, restored):
    m = mse(original, restored)
    if m == 0:
        return 100
    return 20 * np.log10(255.0 / np.sqrt(m))

# -----------------------------
# Print Metrics
# -----------------------------
print("\n📊 Performance Metrics:\n")

print("👉 Gaussian Noise:")
print("Mean Filter   - MSE:", mse(gray, mean_gaussian), "PSNR:", psnr(gray, mean_gaussian))
print("Median Filter - MSE:", mse(gray, median_gaussian), "PSNR:", psnr(gray, median_gaussian))
print("Gaussian Filter - MSE:", mse(gray, gauss_gaussian), "PSNR:", psnr(gray, gauss_gaussian))

print("\n👉 Salt & Pepper Noise:")
print("Mean Filter   - MSE:", mse(gray, mean_sp), "PSNR:", psnr(gray, mean_sp))
print("Median Filter - MSE:", mse(gray, median_sp), "PSNR:", psnr(gray, median_sp))
print("Gaussian Filter - MSE:", mse(gray, gauss_sp), "PSNR:", psnr(gray, gauss_sp))

# -----------------------------
# Save Images
# -----------------------------
cv2.imwrite("outputs/original.png", gray)
cv2.imwrite("outputs/gaussian_noise.png", gaussian_noise)
cv2.imwrite("outputs/sp_noise.png", sp_noise)

cv2.imwrite("outputs/mean_gaussian.png", mean_gaussian)
cv2.imwrite("outputs/median_gaussian.png", median_gaussian)
cv2.imwrite("outputs/gaussian_filtered.png", gauss_gaussian)

cv2.imwrite("outputs/mean_sp.png", mean_sp)
cv2.imwrite("outputs/median_sp.png", median_sp)
cv2.imwrite("outputs/gaussian_sp.png", gauss_sp)

# -----------------------------
# Plot Results
# -----------------------------
titles = [
    "Original", "Gaussian Noise", "Salt & Pepper",
    "Mean (Gaussian)", "Median (Gaussian)", "Gaussian Filter",
    "Mean (SP)", "Median (SP)", "Gaussian (SP)"
]

images = [
    gray, gaussian_noise, sp_noise,
    mean_gaussian, median_gaussian, gauss_gaussian,
    mean_sp, median_sp, gauss_sp
]

plt.figure(figsize=(12, 10))

for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.savefig("outputs/restoration_result.png")
plt.show()

print("\n✅ All outputs saved in 'outputs/' folder")

# -----------------------------
# Observations
# -----------------------------
print("\n📈 Observations:")
print("1. Median filter works best for salt & pepper noise.")
print("2. Gaussian filter works well for Gaussian noise.")
print("3. Mean filter smooths image but blurs details.")
print("4. Median filter preserves edges better.")
print("5. Best filter depends on noise type.")