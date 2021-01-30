import cv2
print('OpenCV version:', cv2.__version__)

img = cv2.imread('./Image/lena.jpg')
# img[y, x]
px = img[100, 98]
print('img[100, 98] 像素的三个通道值', px)
px_blue = img[100, 98, 0]
print('img[100, 98] blue 通道的值:', px_blue)
print('img shape:', img.shape)
print('img type:', img.dtype)
print('img size:', img.size)    # 图像总像素数
# 通道分割与合并
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# 使用numpy索引, 这种方式更好
b = img[:, :, 2]
cv2.imshow('blue', b)
cv2.waitKey(0)

