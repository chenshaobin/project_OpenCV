import cv2
print('OpenCV version:', cv2.__version__)
"""
    # 彩色图是以B-G-R通道顺序进行存储的，灰度图只有一个通道
    # 图像坐标的起始点是左上角，行对应y(高度)，列对应x（宽度）
    # cv2.imread
        # 参数2：默认值：1 彩色图；0 灰度图； -1 包含透明通道的彩色图
"""

img = cv2.imread('./Image/lena.jpg')
# cv2.imshow('lena', img)
# cv2.waitKey(0)
cv2.imwrite('./Image/differentSuffix/lena_bmp.bmp', img)

cv2.imwrite('./Image/differentSuffix/lena_jpg95.jpg', img)
cv2.imwrite('./Image/differentSuffix/lena_jpg20.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 20])
cv2.imwrite('./Image/differentSuffix/lena_jpg100.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

cv2.imwrite('./Image/differentSuffix/lena_png1.png', img)
cv2.imwrite('./Image/differentSuffix/lena_png9.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
