# ============================================================
# Name        : YOUR_NAME_HERE          ← CHANGE THIS
# Roll No     : YOUR_ROLL_NUMBER        ← CHANGE THIS
# Course      : Image Processing & Computer Vision
# Unit        : Image Compression & Segmentation
# Assignment  : Medical Image Compression & Segmentation System
# Date        : DATE_HERE               ← CHANGE THIS (e.g., 24-04-2025)
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
    "images/xray.jpg",   # ← CHANGE: put your actual image filename here
    "images/mri.jpg",    # ← CHANGE: put your actual image filename here
    "images/ct.jpg",     # ← CHANGE: put your actual image filename here
]
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ─────────────────────────────────────────────────────────────
# TASK 1: RUN LENGTH ENCODING (RLE) COMPRESSION
# ─────────────────────────────────────────────────────────────

def rle_encode(image: np.ndarray) -> list:
    """Encode a 2D grayscale image using Run Length Encoding."""
    flat = image.flatten().tolist()
    encoded = []
    count = 1
    for i in range(1, len(flat)):
        if flat[i] == flat[i - 1]:
            count += 1
        else:
            encoded.append((flat[i - 1], count))
            count = 1
    encoded.append((flat[-1], count))
    return encoded


def rle_decode(encoded: list, shape: tuple) -> np.ndarray:
    """Decode RLE back to a 2D image for verification."""
    flat = []
    for value, count in encoded:
        flat.extend([value] * count)
    return np.array(flat, dtype=np.uint8).reshape(shape)


def compression_stats(original: np.ndarray, encoded: list) -> dict:
    """Calculate compression ratio and storage savings."""
    original_size = original.size          # total pixels (each = 1 byte)
    encoded_size  = len(encoded) * 2       # each (value, count) pair = 2 bytes
    ratio         = original_size / encoded_size
    savings       = (1 - encoded_size / original_size) * 100
    return {
        "original_bytes": original_size,
        "encoded_bytes":  encoded_size,
        "compression_ratio": ratio,
        "storage_savings_pct": savings,
    }


def task1_compression(image: np.ndarray, name: str):
    """Run Task 1 pipeline and print results."""
    print("\n" + "="*55)
    print(f"  TASK 1 — RLE Compression  |  {name}")
    print("="*55)

    encoded = rle_encode(image)
    stats   = compression_stats(image, encoded)

    print(f"  Original size    : {stats['original_bytes']:,} bytes")
    print(f"  Encoded size     : {stats['encoded_bytes']:,} bytes")
    print(f"  Compression ratio: {stats['compression_ratio']:.2f}x")
    print(f"  Storage savings  : {stats['storage_savings_pct']:.1f}%")

    # Verify lossless round-trip
    decoded = rle_decode(encoded, image.shape)
    assert np.array_equal(image, decoded), "RLE decode mismatch — check encoder!"
    print("  Lossless check   : ✓ PASSED")

    return stats


# ─────────────────────────────────────────────────────────────
# TASK 2: IMAGE SEGMENTATION (Global + Otsu Thresholding)
# ─────────────────────────────────────────────────────────────

def task2_segmentation(image: np.ndarray, name: str):
    """Apply global and Otsu thresholding."""
    print("\n" + "="*55)
    print(f"  TASK 2 — Image Segmentation  |  {name}")
    print("="*55)

    # Global thresholding — fixed threshold of 127
    global_thresh = 127
    _, seg_global = cv2.threshold(image, global_thresh, 255, cv2.THRESH_BINARY)
    print(f"  Global threshold applied at pixel value: {global_thresh}")

    # Otsu's thresholding — automatic optimal threshold
    otsu_thresh, seg_otsu = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    print(f"  Otsu's optimal threshold calculated   : {otsu_thresh:.1f}")

    return seg_global, seg_otsu, global_thresh, otsu_thresh


# ─────────────────────────────────────────────────────────────
# TASK 3: MORPHOLOGICAL PROCESSING
# ─────────────────────────────────────────────────────────────

def task3_morphology(seg_otsu: np.ndarray, name: str):
    """Apply dilation and erosion to refine segmented regions."""
    print("\n" + "="*55)
    print(f"  TASK 3 — Morphological Processing  |  {name}")
    print("="*55)

    kernel = np.ones((5, 5), np.uint8)

    dilated = cv2.dilate(seg_otsu, kernel, iterations=2)
    eroded  = cv2.erode(seg_otsu, kernel, iterations=2)

    print("  Dilation  : Expanded bright regions (fills small gaps)")
    print("  Erosion   : Shrunk bright regions  (removes small noise)")

    return dilated, eroded


# ─────────────────────────────────────────────────────────────
# TASK 4: ANALYSIS — SAVE FIGURE & CONSOLE DISCUSSION
# ─────────────────────────────────────────────────────────────

def task4_analysis(
    image, seg_global, seg_otsu, dilated, eroded,
    stats, global_thresh, otsu_thresh, name
):
    """Save side-by-side comparison and print clinical discussion."""
    print("\n" + "="*55)
    print(f"  TASK 4 — Analysis & Interpretation  |  {name}")
    print("="*55)

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    fig.suptitle(f"Medical Image Processing Results — {name}", fontsize=14, fontweight="bold")

    panels = [
        (image,      "Original Image",              "gray"),
        (seg_global, f"Global Threshold (T={global_thresh})", "gray"),
        (seg_otsu,   f"Otsu's Threshold (T={otsu_thresh:.0f})",  "gray"),
        (dilated,    "Dilation (k=5×5, iter=2)",    "gray"),
        (eroded,     "Erosion  (k=5×5, iter=2)",    "gray"),
    ]

    for ax, (img, title, cmap) in zip(axes.flat, panels):
        ax.imshow(img, cmap=cmap)
        ax.set_title(title, fontsize=10)
        ax.axis("off")

    # Last panel: compression stats text
    ax = axes.flat[5]
    ax.axis("off")
    summary = (
        f"Compression Summary\n"
        f"{'─'*28}\n"
        f"Original : {stats['original_bytes']:,} B\n"
        f"Encoded  : {stats['encoded_bytes']:,} B\n"
        f"Ratio    : {stats['compression_ratio']:.2f}×\n"
        f"Savings  : {stats['storage_savings_pct']:.1f}%\n\n"
        f"Clinical Note:\n"
        f"Otsu's method adaptively\n"
        f"segments ROI (tissue/tumour)\n"
        f"without manual tuning.\n"
        f"Morphology refines edges\n"
        f"for diagnosis support."
    )
    ax.text(0.05, 0.95, summary, transform=ax.transAxes,
            fontsize=9, verticalalignment="top", family="monospace")

    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, f"{name}_results.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"  Comparison figure saved → {out_path}")

    print("\n  CLINICAL RELEVANCE DISCUSSION")
    print("  ─────────────────────────────────────────────────")
    print("  • Global thresholding uses a fixed cutoff which may")
    print("    miss subtle intensity variations in MRI/CT scans.")
    print("  • Otsu's method picks the optimal threshold automatically,")
    print("    making it robust across different imaging modalities.")
    print("  • Dilation helps close small gaps inside organ boundaries,")
    print("    useful when highlighting tumour margins.")
    print("  • Erosion removes tiny noise artifacts that can otherwise")
    print("    be misidentified as pathological regions.")
    print("  ─────────────────────────────────────────────────")


# ─────────────────────────────────────────────────────────────
# MAIN — PROCESS ALL THREE IMAGES
# ─────────────────────────────────────────────────────────────

def save_intermediate(image, filename):
    """Save individual output images to the outputs/ folder."""
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), image)


def process_image(path: str):
    """Full pipeline for a single medical image."""
    name = Path(path).stem          # e.g., "xray"
    print(f"\n{'#'*55}")
    print(f"  Processing image: {path}")
    print(f"{'#'*55}")

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"  ⚠ Could not load '{path}'. Skipping.")
        return

    print(f"  Image shape: {image.shape}  |  dtype: {image.dtype}")

    # Save original
    save_intermediate(image, f"{name}_original.png")

    # Task 1
    stats = task1_compression(image, name)

    # Task 2
    seg_global, seg_otsu, g_t, o_t = task2_segmentation(image, name)
    save_intermediate(seg_global, f"{name}_global_threshold.png")
    save_intermediate(seg_otsu,   f"{name}_otsu_threshold.png")

    # Task 3
    dilated, eroded = task3_morphology(seg_otsu, name)
    save_intermediate(dilated, f"{name}_dilated.png")
    save_intermediate(eroded,  f"{name}_eroded.png")

    # Task 4
    task4_analysis(image, seg_global, seg_otsu, dilated, eroded,
                   stats, g_t, o_t, name)


def main():
    print("\n" + "★"*55)
    print("  Medical Image Compression & Segmentation System")
    print("  Course: Image Processing & Computer Vision")
    print("★"*55)

    for img_path in INPUT_IMAGES:
        process_image(img_path)

    print(f"\n✅ All outputs saved in '{OUTPUT_DIR}/' folder.")
    print("   Done! Happy coding.\n")


if __name__ == "__main__":
    main()