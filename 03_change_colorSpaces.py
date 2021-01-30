import cv2
print('OpenCV version:', cv2.__version__)

img = cv2.imread('./Image/lena.jpg')
# 转换为灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', img)
# cv2.imshow('gray', img_gray)
# cv2.waitKey(0)

# 所有的转换模式
flag = [i for i in dir(cv2) if i.startswith('COLOR_')]
print('转换模式:', flag)