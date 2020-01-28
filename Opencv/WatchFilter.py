import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMWRITE_JPEG_CHROMA_QUALITY)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

cv2.imwrite('Yenisaat.png',img)