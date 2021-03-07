"""
    # Date:2021.03.06
    # 仿射变换：
        # 主要包括平移变换、旋转变换、尺度变换、倾斜变换（也叫错切变换、剪切变换、偏移变换）、翻转变换，一共有六个自由度
        # 基于2x3矩阵
        # 平移包括x方向平移和y方向平移，自由度为2
    # 刚体变换（也称欧式变换）
        # 变换前后两点间的距离仍保持不变
        # 包括了平移、旋转和翻转，自由度为3
    # 相似变换
        # 包含旋转、等比例缩放和平移等变换，自由度为4
        # 相比刚体变换加了缩放，所以并不会保持欧式距离不变，但直线间的夹角依然不变。
    # 透视变换（Perspective Transformation）
        # 也称为投影映射（Projective Mapping）
        # 将二维的图片投影到一个三维视平面上，然后再转换到二维坐标下
        # 变换矩阵为3x3
        # 自由度为8，变换后产生新的四边形，需要四个非共线的四个点才能唯一确定，透视变换包括了所有的仿射变换
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1.仿射变换
img = cv2.imread('./Image/drawing.jpg')
rows, cols = img.shape[:2]

# 变换前的三个点
pts1 = np.float32([[50, 65], [150, 65], [210, 210]])
# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])
# 生成变换矩阵
M = cv2.getAffineTransform(pts1, pts2)
print('仿射变换矩阵:', M)
dst = cv2.warpAffine(img, M, (rows, cols))
# 转换图像的通道顺序
img = img[:,:,::-1]
dst = dst[:,:,::-1]
plt.subplot(121), plt.imshow(img), plt.title('input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show()

# 2.透视变换
img2 = cv2.imread('./Image/card.jpg')
# 原图中的四个角点
pts3 = np.float32([[148, 80], [437, 114], [94, 247], [423, 288]])
# 变换后图片中的对应点
pts4 = np.float32([[0, 0], [320, 0], [0, 178], [320, 178]])
# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts3, pts4)
print('透视变换矩阵：', M)
# 进行透视变换，参数3是目标图像的大小
dst2 = cv2.warpPerspective(img2, M, (320, 178))
plt.subplot(121), plt.imshow(img2[:,:,::-1]), plt.title('input')
plt.subplot(122), plt.imshow(dst2[:,:,::-1]), plt.title('output')
plt.show()
