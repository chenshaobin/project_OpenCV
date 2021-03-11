import cv2
import numpy as np
import matplotlib.pyplot as plt

def track_back(x):
    # x:表示当前值的参数
    pass

img = cv2.imread('../Image/sudoku.jpg', 0)
cv2.namedWindow('cannyWindow')

# 创建滑动条
cv2.createTrackbar('maxVal', 'cannyWindow', 100, 255, track_back)
cv2.createTrackbar('minVal', 'cannyWindow', 200, 255, track_back)

while(True):
    max_val = cv2.getTrackbarPos('maxVal', 'cannyWindow')
    min_val = cv2.getTrackbarPos('minVal', 'cannyWindow')
    edges = cv2.Canny(img, min_val, max_val)
    cv2.imshow('cannyWindow', edges)
    # 按下ESC键退出
    if cv2.waitKey(30) == 27:
        break
