import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "foto.jpg"
img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaussian = cv2.GaussianBlur(gray, (7, 7), 0)

plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1), plt.imshow(gray, cmap='gray'), plt.title("Citra Asli Grayscale")
plt.subplot(1, 3, 2), plt.imshow(gaussian, cmap='gray'), plt.title("Setelah Gaussian Filter")

cv2.imwrite("hasil_gaussian.jpg", gaussian)

plt.tight_layout()
plt.show()
