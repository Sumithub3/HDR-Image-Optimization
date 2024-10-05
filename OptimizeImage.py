# https://github.com/Sumithub3/HDR-Image-Optimization.git

import os

import cv2 as cv
import numpy as np

UPLOAD_FOLDER = 'uploads'
SCANNED_IMAGE_FOLDER = "Static\\scanned_Images"

class ImageOptimization:
    def __init__(self):
        pass
    def optimize_image(image_path):
        img = cv.imread(image_path)

        if img is None:
            raise ValueError("Could not load image!")

        img_float = np.float32(img) / 255.0
        img_dark = cv.convertScaleAbs(img_float, alpha=0.3, beta=0)  # Simulated darker exposure
        img_bright = cv.convertScaleAbs(img_float, alpha=1.1, beta=0)  # Simulated brighter exposure
        img_list = [img_dark, img_float, img_bright]

        img_list_float32 = [np.float32(img) for img in img_list]
        tonemap_mantiuk = cv.createTonemapMantiuk(scale=0.85, saturation=1.9)
        ldr_mantiuk = tonemap_mantiuk.process(img_list_float32[1])  # Using the middle image for tone mapping
        ldr_mantiuk_8bit = np.clip(ldr_mantiuk * 255, 0, 255).astype('uint8')

        smooth_img = cv.GaussianBlur(ldr_mantiuk_8bit, (3, 3), 0)
        sharp_img = cv.addWeighted(ldr_mantiuk_8bit, 3.7, smooth_img, -0.5, 10)

        output_path = os.path.join(SCANNED_IMAGE_FOLDER, 'optimized_' + os.path.basename(image_path))
        cv.imwrite(output_path, sharp_img)

        return output_path
