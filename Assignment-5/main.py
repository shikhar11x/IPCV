# =============================================================================
# Student Name  : [Your Name]
# Roll No       : [Your Roll No]
# Course Name   : Image Processing & Computer Vision
# Assignment    : Designing an End-to-End Intelligent Image Processing System
# Date          : [Submission Date]
# =============================================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse

# ── Output directory ──────────────────────────────────────────────────────────
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# TASK 1 – Welcome Banner
# =============================================================================

def print_banner():
    print("=" * 65)
    print("   INTELLIGENT IMAGE ENHANCEMENT & ANALYSIS SYSTEM")
    print("=" * 65)
    print("  Purpose : End-to-end image processing pipeline")
    print("  Stages  : Acquisition → Enhancement → Restoration →")
    print("            Segmentation → Feature Extraction → Evaluation")
    print("=" * 65)
    print()

# =============================================================================
# TASK 2 – Image Acquisition & Preprocessing
# =============================================================================

def load_image(image_path: str) -> tuple[np.ndarray, np.ndarray]:
    """Load, resize to 512×512, and convert to grayscale."""
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        raise FileNotFoundError(f"Cannot load image: '{image_path}'")

    img_bgr   = cv2.resize(img_bgr, (512, 512))
    img_rgb   = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Display
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].imshow(img_rgb);  axes[0].set_title("Original (colour)"); axes[0].axis("off")
    axes[1].imshow(img_gray, cmap="gray"); axes[1].set_title("Grayscale"); axes[1].axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "01_acquisition.png"), dpi=150)
    plt.close()
    print("[Task 2] Acquisition complete — saved 01_acquisition.png")
    return img_rgb, img_gray

# =============================================================================
# TASK 3 – Image Enhancement & Restoration
# =============================================================================

def add_gaussian_noise(img: np.ndarray, sigma: float = 25.0) -> np.ndarray:
    noise = np.random.normal(0, sigma, img.shape).astype(np.float32)
    return np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(img: np.ndarray, amount: float = 0.04) -> np.ndarray:
    noisy = img.copy()
    n_total = int(amount * img.size)
    # Salt
    coords = [np.random.randint(0, d, n_total // 2) for d in img.shape]
    noisy[coords[0], coords[1]] = 255
    # Pepper
    coords = [np.random.randint(0, d, n_total // 2) for d in img.shape]
    noisy[coords[0], coords[1]] = 0
    return noisy

def enhance_and_restore(gray: np.ndarray) -> dict[str, np.ndarray]:
    """Add noise, apply filters, apply CLAHE."""
    gauss_noisy = add_gaussian_noise(gray)
    sp_noisy    = add_salt_pepper_noise(gray)

    mean_filtered   = cv2.blur(gauss_noisy, (5, 5))
    median_filtered = cv2.medianBlur(sp_noisy, 5)
    gauss_filtered  = cv2.GaussianBlur(gauss_noisy, (5, 5), 0)

    clahe   = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(median_filtered)

    images = {
        "Gaussian Noisy": gauss_noisy,
        "S&P Noisy":      sp_noisy,
        "Mean Filtered":  mean_filtered,
        "Median Filtered": median_filtered,
        "Gaussian Filtered": gauss_filtered,
        "CLAHE Enhanced": enhanced,
    }

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for ax, (title, img) in zip(axes.flat, images.items()):
        ax.imshow(img, cmap="gray"); ax.set_title(title); ax.axis("off")
    plt.suptitle("Task 3 – Enhancement & Restoration", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "02_enhancement.png"), dpi=150)
    plt.close()
    print("[Task 3] Enhancement complete — saved 02_enhancement.png")
    return {"sp_noisy": sp_noisy, "gauss_noisy": gauss_noisy,
            "restored": median_filtered, "enhanced": enhanced}

# =============================================================================
# TASK 4 – Segmentation & Morphological Processing
# =============================================================================

def segment_and_morph(enhanced: np.ndarray) -> dict[str, np.ndarray]:
    # Thresholding
    _, global_thresh = cv2.threshold(enhanced, 127, 255, cv2.THRESH_BINARY)
    _, otsu_thresh   = cv2.threshold(enhanced, 0, 255,
                                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel   = np.ones((5, 5), np.uint8)
    dilated  = cv2.dilate(otsu_thresh, kernel, iterations=1)
    eroded   = cv2.erode(otsu_thresh,  kernel, iterations=1)

    images = {
        "Global Threshold": global_thresh,
        "Otsu Threshold":   otsu_thresh,
        "Dilation":         dilated,
        "Erosion":          eroded,
    }

    fig, axes = plt.subplots(2, 2, figsize=(10, 9))
    for ax, (title, img) in zip(axes.flat, images.items()):
        ax.imshow(img, cmap="gray"); ax.set_title(title); ax.axis("off")
    plt.suptitle("Task 4 – Segmentation & Morphology", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "03_segmentation.png"), dpi=150)
    plt.close()
    print("[Task 4] Segmentation complete — saved 03_segmentation.png")
    return {"segmented": otsu_thresh, "dilated": dilated, "eroded": eroded}

# =============================================================================
# TASK 5 – Object Representation & Feature Extraction
# =============================================================================

def extract_features(gray: np.ndarray, enhanced: np.ndarray) -> dict[str, np.ndarray]:
    # Edge detection
    sobelx  = cv2.Sobel(enhanced, cv2.CV_64F, 1, 0, ksize=5)
    sobely  = cv2.Sobel(enhanced, cv2.CV_64F, 0, 1, ksize=5)
    sobel   = cv2.magnitude(sobelx, sobely)
    sobel   = np.clip(sobel, 0, 255).astype(np.uint8)
    canny   = cv2.Canny(enhanced, 100, 200)

    # Contours & bounding boxes on the Canny result
    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bbox_img = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    for cnt in contours:
        if cv2.contourArea(cnt) > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(bbox_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    bbox_img = cv2.cvtColor(bbox_img, cv2.COLOR_BGR2RGB)

    # ORB keypoints
    orb = cv2.ORB_create(nfeatures=500)
    kp, _ = orb.detectAndCompute(enhanced, None)
    kp_img = cv2.drawKeypoints(enhanced, kp, None,
                               flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    kp_img = cv2.cvtColor(kp_img, cv2.COLOR_BGR2RGB)

    print(f"[Task 5] ORB keypoints detected: {len(kp)}")

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    panels = [
        ("Sobel Edges",       sobel,    "gray"),
        ("Canny Edges",       canny,    "gray"),
        ("Bounding Boxes",    bbox_img, None),
        ("ORB Keypoints",     kp_img,   None),
    ]
    for ax, (title, img, cmap) in zip(axes.flat, panels):
        ax.imshow(img, cmap=cmap); ax.set_title(title); ax.axis("off")
    plt.suptitle("Task 5 – Feature Extraction", fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "04_features.png"), dpi=150)
    plt.close()
    print("[Task 5] Feature extraction complete — saved 04_features.png")
    return {"sobel": sobel, "canny": canny}

# =============================================================================
# TASK 6 – Performance Evaluation
# =============================================================================

def evaluate(original: np.ndarray, enhanced: np.ndarray, restored: np.ndarray):
    def metrics(ref, img, label):
        m   = mse(ref, img)
        p   = psnr(ref, img, data_range=255)
        s   = ssim(ref, img, data_range=255)
        print(f"  {label:28s}  MSE={m:8.2f}  PSNR={p:6.2f} dB  SSIM={s:.4f}")
        return m, p, s

    print("\n[Task 6] Performance Evaluation")
    print("  " + "-" * 65)
    m1, p1, s1 = metrics(original, enhanced, "Original vs Enhanced")
    m2, p2, s2 = metrics(original, restored, "Original vs Restored")
    print("  " + "-" * 65)

    categories = ["Original vs Enhanced", "Original vs Restored"]
    mse_vals  = [m1, m2]
    psnr_vals = [p1, p2]
    ssim_vals = [s1, s2]

    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, vals, title in zip(axes,
                               [mse_vals, psnr_vals, ssim_vals],
                               ["MSE (lower better)", "PSNR dB (higher better)",
                                "SSIM (closer to 1)"]):
        bars = ax.bar(categories, vals, color=["steelblue", "darkorange"])
        ax.set_title(title); ax.set_xticklabels(categories, rotation=12, ha="right")
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    f"{v:.3f}", ha="center", va="bottom", fontsize=9)
    plt.suptitle("Task 6 – Quality Metrics", fontsize=13)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "05_metrics.png"), dpi=150)
    plt.close()
    print("[Task 6] Metrics chart saved — 05_metrics.png")

# =============================================================================
# TASK 7 – Final Pipeline Visualisation
# =============================================================================

def final_pipeline(original_gray, noisy, restored, enhanced, segmented, feature):
    stages = [
        ("Original",  original_gray, "gray"),
        ("Noisy",     noisy,         "gray"),
        ("Restored",  restored,      "gray"),
        ("Enhanced",  enhanced,      "gray"),
        ("Segmented", segmented,     "gray"),
        ("Edges",     feature,       "gray"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    for ax, (title, img, cmap) in zip(axes.flat, stages):
        ax.imshow(img, cmap=cmap); ax.set_title(title, fontsize=13); ax.axis("off")
    plt.suptitle("Task 7 – Complete Processing Pipeline", fontsize=15, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "06_pipeline.png"), dpi=150)
    plt.close()
    print("[Task 7] Pipeline visualization saved — 06_pipeline.png")

    print("\n" + "=" * 65)
    print("  CONCLUSION")
    print("=" * 65)
    print("  • Median filtering outperforms mean/Gaussian on S&P noise.")
    print("  • CLAHE improves local contrast without over-brightening.")
    print("  • Otsu thresholding produces cleaner segments than global.")
    print("  • Canny edges are sharper and less noisy than Sobel alone.")
    print("  • ORB keypoints are scale/rotation invariant and fast.")
    print("  • PSNR & SSIM together give a reliable quality estimate.")
    print("=" * 65)

# =============================================================================
# ENTRY POINT
# =============================================================================

def main():
    print_banner()

    # Accept image path as CLI arg or prompt the user
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = input("Enter path to input image (e.g., images/input.jpg): ").strip()

    print(f"\nProcessing: {image_path}\n")

    img_rgb, img_gray = load_image(image_path)

    t3 = enhance_and_restore(img_gray)
    t4 = segment_and_morph(t3["enhanced"])
    t5 = extract_features(img_gray, t3["enhanced"])

    evaluate(img_gray, t3["enhanced"], t3["restored"])

    final_pipeline(
        original_gray = img_gray,
        noisy         = t3["sp_noisy"],
        restored      = t3["restored"],
        enhanced      = t3["enhanced"],
        segmented     = t4["segmented"],
        feature       = t5["canny"],
    )

    print(f"\nAll outputs saved to: ./{OUTPUT_DIR}/")

if __name__ == "__main__":
    main()