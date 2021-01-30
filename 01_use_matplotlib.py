import cv2
import matplotlib.pyplot as plt
import matplotlib.image as pli
print('OpenCV version:', cv2.__version__)
img = cv2.imread('./Image/lena.jpg')
# 在matplotlib中是以RGB模式显示图片的，所以需要转换通道顺序
img2 = img[:, :, ::-1]
"""
plt.subplot(121)
plt.imshow(img) 
plt.subplot(122)
plt.xticks([]), plt.yticks([])
plt.imshow(img2)
plt.show()
"""

img_pli = pli.imread('./Image/lena.jpg')
plt.imshow(img_pli)
plt.savefig('./Image/lena_pli.jpg')
plt.show()