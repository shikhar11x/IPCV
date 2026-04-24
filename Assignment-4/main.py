# ============================================================
# Name        : Shikhar Bajpai
# Roll No     : 2301010188
# Course      : Image Processing & Computer Vision
# Unit        : Object Representation & Feature Extraction
# Assignment  : Feature-Based Traffic Monitoring System
# Date        : DATE_HERE               ← CHANGE THIS
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────
INPUT_IMAGES = [
    "images/traffic1.jpg",   # ← CHANGE: road intersection image
    "images/traffic2.jpg",   # ← CHANGE: highway image
    "images/traffic3.jpg",   # ← CHANGE: pedestrian crossing image
]
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ─────────────────────────────────────────────────────────────
# TASK 1: EDGE DETECTION (Sobel + Canny)
# ─────────────────────────────────────────────────────────────

def task1_edge_detection(image: np.ndarray, name: str):
    """Apply Sobel and Canny edge detection and compare results."""
    print("\n" + "="*55)
    print(f"  TASK 1 — Edge Detection  |  {name}")
    print("="*55)

    # Sobel operator — detects horizontal and vertical gradients
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel   = cv2.magnitude(sobel_x, sobel_y)
    sobel   = np.uint8(np.clip(sobel, 0, 255))

    # Canny edge detector — multi-stage, gives cleaner edges
    canny = cv2.Canny(image, threshold1=50, threshold2=150)

    sobel_edges = np.count_nonzero(sobel > 30)
    canny_edges = np.count_nonzero(canny > 0)

    print(f"  Sobel edge pixels : {sobel_edges:,}")
    print(f"  Canny edge pixels : {canny_edges:,}")
    print(f"  Canny detects sharper, cleaner boundaries than Sobel.")

    return sobel, canny


# ─────────────────────────────────────────────────────────────
# TASK 2: OBJECT REPRESENTATION (Contours + Bounding Boxes)
# ─────────────────────────────────────────────────────────────

def task2_object_representation(image: np.ndarray, canny: np.ndarray, name: str):
    """Detect contours, draw bounding boxes, compute area and perimeter."""
    print("\n" + "="*55)
    print(f"  TASK 2 — Object Representation  |  {name}")
    print("="*55)

    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter small noise contours (area < 500 pixels)
    contours = [c for c in contours if cv2.contourArea(c) > 500]

    # Draw on color copy
    contour_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    bbox_img    = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

    print(f"  Objects detected  : {len(contours)}")
    print(f"  {'#':<4} {'Area (px²)':<14} {'Perimeter (px)'}")
    print(f"  {'─'*36}")

    for i, c in enumerate(contours[:10]):   # print top 10
        area      = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, closed=True)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(bbox_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print(f"  {i+1:<4} {area:<14.1f} {perimeter:.1f}")

    return contour_img, bbox_img, contours


# ─────────────────────────────────────────────────────────────
# TASK 3: FEATURE EXTRACTION (ORB)
# ─────────────────────────────────────────────────────────────

def task3_feature_extraction(image: np.ndarray, name: str):
    """Extract keypoints and descriptors using ORB."""
    print("\n" + "="*55)
    print(f"  TASK 3 — Feature Extraction  |  {name}")
    print("="*55)

    # ORB — free alternative to SIFT/SURF (no patent issues)
    orb = cv2.ORB_create(nfeatures=500)
    keypoints, descriptors = orb.detectAndCompute(image, None)

    orb_img = cv2.drawKeypoints(
        image, keypoints, None,
        color=(0, 255, 0),
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    print(f"  ORB keypoints found    : {len(keypoints)}")
    if descriptors is not None:
        print(f"  Descriptor shape       : {descriptors.shape}  (keypoints × 32 bytes)")
    print(f"  ORB is rotation & scale invariant — suitable for traffic monitoring.")

    return orb_img, keypoints


# ─────────────────────────────────────────────────────────────
# TASK 4: COMPARATIVE ANALYSIS — SAVE FIGURE
# ─────────────────────────────────────────────────────────────

def task4_analysis(
    image, sobel, canny,
    contour_img, bbox_img,
    orb_img, keypoints, contours,
    name
):
    """Save side-by-side comparison figure and print analysis."""
    print("\n" + "="*55)
    print(f"  TASK 4 — Comparative Analysis  |  {name}")
    print("="*55)

    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle(f"Traffic Monitoring Results — {name}", fontsize=14, fontweight="bold")

    panels = [
        (image,                        "Original (Grayscale)",      "gray"),
        (sobel,                        "Sobel Edge Detection",       "gray"),
        (canny,                        "Canny Edge Detection",       "gray"),
        (cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB), "Contours Detected", None),
        (cv2.cvtColor(bbox_img,    cv2.COLOR_BGR2RGB), "Bounding Boxes",    None),
        (cv2.cvtColor(orb_img,     cv2.COLOR_BGR2RGB), f"ORB Keypoints ({len(keypoints)})", None),
    ]

    for ax, (img, title, cmap) in zip(axes.flat, panels):
        ax.imshow(img, cmap=cmap)
        ax.set_title(title, fontsize=10)
        ax.axis("off")

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, f"{name}_results.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"  Comparison figure saved → {out_path}")

    print("\n  EDGE DETECTOR COMPARISON")
    print("  ─────────────────────────────────────────────────")
    print("  • Sobel highlights intensity gradients in X and Y")
    print("    directions. It is fast but sensitive to noise.")
    print("  • Canny uses Gaussian smoothing + double thresholding,")
    print("    producing thin, accurate edges — better for contour")
    print("    detection in cluttered traffic scenes.")

    print("\n  FEATURE EXTRACTOR — ORB")
    print("  ─────────────────────────────────────────────────")
    print("  • ORB (Oriented FAST + Rotated BRIEF) detects stable")
    print("    keypoints regardless of rotation or scale change.")
    print("  • In traffic monitoring, ORB features can match the")
    print("    same vehicle across frames — enabling tracking.")
    print("  • ORB is patent-free and fast, making it suitable")
    print("    for real-time surveillance applications.")
    print("  ─────────────────────────────────────────────────")


# ─────────────────────────────────────────────────────────────
# MAIN — PROCESS ALL THREE IMAGES
# ─────────────────────────────────────────────────────────────

def save_output(image, filename):
    """Save an individual output image."""
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), image)


def process_image(path: str):
    """Full pipeline for a single traffic image."""
    name  = Path(path).stem
    print(f"\n{'#'*55}")
    print(f"  Processing: {path}")
    print(f"{'#'*55}")

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"  ⚠ Could not load '{path}'. Skipping.")
        return

    image = cv2.resize(image, (512, 512))
    print(f"  Image shape : {image.shape}  |  dtype: {image.dtype}")

    save_output(image, f"{name}_original.png")

    # Task 1
    sobel, canny = task1_edge_detection(image, name)
    save_output(sobel, f"{name}_sobel.png")
    save_output(canny, f"{name}_canny.png")

    # Task 2
    contour_img, bbox_img, contours = task2_object_representation(image, canny, name)
    save_output(contour_img, f"{name}_contours.png")
    save_output(bbox_img,    f"{name}_bboxes.png")

    # Task 3
    orb_img, keypoints = task3_feature_extraction(image, name)
    save_output(orb_img, f"{name}_orb_keypoints.png")

    # Task 4
    task4_analysis(image, sobel, canny, contour_img, bbox_img, orb_img, keypoints, contours, name)


def main():
    print("\n" + "★"*55)
    print("  Feature-Based Traffic Monitoring System")
    print("  Course: Image Processing & Computer Vision")
    print("★"*55)

    for img_path in INPUT_IMAGES:
        process_image(img_path)

    print(f"\n✅ All outputs saved in '{OUTPUT_DIR}/' folder.")
    print("   Done! Happy coding.\n")


if __name__ == "__main__":
    main()