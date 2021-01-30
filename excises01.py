import cv2
print('OpenCV version:', cv2.__version__)
"""
    # 读取图片，按下‘s’，就保存图片
"""
img = cv2.imread('./Image/lena.jpg')
cv2.namedWindow('lena', cv2.WINDOW_NORMAL)
cv2.imshow('lena', img)
k = cv2.waitKey(0)
print('按下的键：', k)
if k == ord('s'):
    cv2.imwrite('./Image/lena_save_with_key_s.bmp', img)
    print('已经保存图片.')

