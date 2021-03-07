"""
    # Date: 2021.03.07
    # Subject: 模糊/平滑图片来消除图片噪声
    # 滤波与模糊
        # 它们都属于卷积，不同滤波方法之间只是卷积核不同（对线性滤波而言）
        # 低通滤波器是模糊，高通滤波器是锐化
        # 低通滤波器就是允许低频信号通过，在图像中边缘和噪点都相当于高频部分，所以低通滤波器用于去除噪点、平滑和模糊图像。
        # 高通滤波器则反之，用来增强图像边缘，进行锐化处理。效率相比于均值滤波要慢，但可以有效消除高斯噪声，能保留更多的图像细节
    # 中值滤波：适用于去除椒盐噪声和斑点噪声，非线性操作
    # 双边滤波器： 可以保留更多的边缘信息
    # 小结
        在不知道用什么滤波器好的时候，优先高斯滤波cv2.GaussianBlur()，然后均值滤波cv2.blur()。
        斑点和椒盐噪声优先使用中值滤波cv2.medianBlur()。
        要去除噪点的同时尽可能保留更多的边缘信息，使用双边滤波cv2.bilateralFilter()。
        线性滤波方式：均值滤波、方框滤波、高斯滤波（速度相对快）。
        非线性滤波方式：中值滤波、双边滤波（速度相对慢）。

"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
# 1 均值滤波,实现模糊操作
img = cv2.imread('./Image/lena.jpg')
# blur = cv2.blur(img, (3, 3), borderType=cv2.BORDER_DEFAULT)
# 方框滤波也能实现均值滤波, 当参数normalize为False时，相当于求区域内的像素和
blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# plt.subplot(121), plt.imshow(img[:,:,::-1]), plt.title('Original')
# plt.subplot(122), plt.imshow(blur[:, :, ::-1]), plt.title('blur')
# plt.show()

# 高斯滤波
img2 = cv2.imread('./Image/gaussian_noise.bmp')
blur = cv2.blur(img2, (5, 5), borderType=cv2.BORDER_DEFAULT)
gaussian = cv2.GaussianBlur(img2, (5, 5), 1)    # 第三个参数代表方差，值越大，模糊效果越明显，但是效率较慢
# res = np.hstack((img2, blur, gaussian))
# cv2.imshow('res', res)
# cv2.waitKey(0)

# 中值滤波
img3 = cv2.imread('./Image/salt_noise.bmp')
blur = cv2.blur(img3, (5, 5), borderType=cv2.BORDER_DEFAULT)
gaussian = cv2.GaussianBlur(img3, (5, 5), 1)
median = cv2.medianBlur(img3, 5)
# res = np.hstack((img3, blur, gaussian, median))
# cv2.imshow('blur vs gaussian vs median', res)
# cv2.waitKey(0)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
blur = cv2.bilateralFilter(img, 9, 75, 75)
# res = np.hstack((img, blur, gaussian))
# cv2.imshow('blur vs gaussian', res)
# cv2.waitKey(0)
print(cv2.getGaussianKernel(3, 0))


