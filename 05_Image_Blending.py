"""
    # Date:2021.03.07
    # 图像间的数学运算
        # 图片相加: 直接相加会改变图片颜色，用图像混合会改变图像的透明度
        # 按位操作: cv2.bitwise_and(), cv2.bitwise_not(), cv2.bitwise_or(),cv2.bitwise_xor()

"""
import cv2
import matplotlib.pyplot as plt


# 1 图像混合
"""
img1 = cv2.imread('./Image/lena_small.jpg')
img2 = cv2.imread('./Image/opencv-logo-white.png')
# res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
res = cv2.addWeighted(img1, 1, img2, 1, 0)
cv2.imshow('blending', res)
cv2.waitKey(0)
"""

# 2 按位操作
img2 = cv2.imread('./Image/opencv-logo-white.png')
# plt.subplot(122), plt.imshow(img2[:,:, ::-1]), plt.title('img2')
# plt.show()
img3 = cv2.imread('./Image/lena.jpg')
# 将logo放在左上角,
rows, cols = img2.shape[:2]
roi = img3[:rows, :cols]
# 创建掩模
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# plt.subplot(121), plt.imshow(img2[:,:,::-1]), plt.title('Original')
# plt.subplot(122), plt.imshow(img2gray, cmap ='gray'), plt.title('gray')
# plt.show()

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# plt.subplot(122), plt.imshow(mask, cmap ='gray'), plt.title('mask')
# plt.show()
# cv2.imshow('mask', mask)
# cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
# plt.subplot(122), plt.imshow(mask_inv, cmap ='gray'), plt.title('mask')
# plt.show()
# 保留除logo外的背景
img3_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
plt.subplot(122), plt.imshow(img3_bg[:,:, ::-1]), plt.title('img3_bg')
plt.show()
# 进行融合
dst = cv2.add(img3_bg, img2)
plt.subplot(122), plt.imshow(dst[:,:, ::-1]), plt.title('add logo')
plt.show()
# 把融合后的图片放到原图上
img3[:rows, :cols] = dst
plt.subplot(122), plt.imshow(img3[:,:, ::-1]), plt.title('Blending Image')
plt.show()
