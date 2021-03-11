"""
    # Sobel算子
        先在垂直方向上计算梯度，再在水平方向上计算梯度，最后求出总梯度
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./Image/2_176.jpg', 0)
kernel = np.array([-1,0,1,-2,0,2,-1,0,1], dtype=np.float32).reshape(3,3)
# print(kernel)
dst_vertical = cv2.filter2D(img, -1, kernel)
# print(dst_vertical)
dst_herizontal = cv2.filter2D(img, -1, kernel.T)
img_channel3 = np.concatenate((np.expand_dims(img, axis=2),np.expand_dims(img, axis=2), np.expand_dims(img, axis=2)), axis=-1)
"""
plt.subplot(131), plt.imshow(img_channel3, cmap='gray'), plt.title('original Img')
plt.subplot(132), plt.imshow(dst_vertical, cmap='gray'), plt.title('vertical edge')
plt.subplot(133), plt.imshow(dst_herizontal, cmap='gray'), plt.title('horizontal edge')
plt.show()
"""
# 以上这种差分方法就叫Sobel算子
sobelx = cv2.Sobel(img,-1, 1, 0, ksize=3)
sobley = cv2.Sobel(img, -1, 0, 1, ksize=3)
soblexy = cv2.Sobel(img, -1, 1, 1, ksize=3)
"""
plt.subplot(141), plt.imshow(img_channel3, cmap='gray'), plt.title('original Img')
plt.subplot(142), plt.imshow(sobelx, cmap='gray'), plt.title('vertical edge')
plt.subplot(143), plt.imshow(sobley, cmap='gray'), plt.title('horizontal edge')
plt.subplot(144), plt.imshow(soblexy, cmap='gray'), plt.title('x y edge')
plt.show()
"""

laplacian = cv2.Laplacian(img,-1)
plt.subplot(121), plt.imshow(img_channel3, cmap='gray'), plt.title('original Img')
plt.subplot(122), plt.imshow(laplacian, cmap='gray'), plt.title('laplacian Img')
plt.show()