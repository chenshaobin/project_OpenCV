"""
    # Canny 边缘检测
        推荐的高低阈值比在2:1到3:1之间
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Image/handwriting.jpg', 0)     # 参数0读取灰度图
edge = cv2.Canny(img, 30, 70)

# cv2.imshow('candy', np.hstack((img, edge)))
# cv2.waitKey(0)

## 把单通道的灰度图转换成三通道的灰度图
print('img shape:', img.shape)
imgOfThree = np.concatenate((np.expand_dims(img, axis=2), np.expand_dims(img, axis=2), np.expand_dims(img, axis=2)), axis=-1)

# plt.subplot(121), plt.imshow(imgOfThree, cmap='gray'), plt.title('Original')
# plt.subplot(122), plt.imshow(edge, cmap='gray'), plt.title('edge')
# plt.show()

# 阈值分割后再检测边缘，效果会更好
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(thresh, 30, 70)
plt.subplot(121), plt.imshow(edges, cmap='gray'), plt.title('threshold_canny')
plt.subplot(122), plt.imshow(edge, cmap='gray'), plt.title('canny')
plt.show()