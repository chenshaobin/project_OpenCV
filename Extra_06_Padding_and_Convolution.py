import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./Image/6_by_6.bmp', 0)
print(img)
# 给图片添加边框
# 1 固定值边框
cons = cv2.copyMakeBorder(img, 1,1,1,1, cv2.BORDER_CONSTANT, value=0)
print(cons)
# 2 默认边框
default = cv2.copyMakeBorder(img, 1,1,1,1,cv2.BORDER_DEFAULT)
print(default)
# 使用卷积对图像进行模糊处理
img2 = cv2.imread('./Image/lena.jpg')
kernel = np.ones((3,3), np.float32) / 10
# 卷积操作， -1表示通道数与原图相同
dst = cv2.filter2D(img2, -1, kernel)
plt.subplot(121), plt.imshow(img2[:,:,::-1]), plt.title('Original Img')
plt.subplot(122), plt.imshow(dst[:,:,::-1]), plt.title('Filter Img')
plt.show()

