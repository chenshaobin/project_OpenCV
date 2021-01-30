import cv2
print('OpenCV version:', cv2.__version__)
import numpy as np

# Gray scale
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = 0.299 * r + 0.587 * g + 0.114 * b
    out = out.astype(np.uint8)

    return out

img = cv2.imread('./Image/imori.jpg')
img_gray = BGR2GRAY(img)
# cv2.imwrite('./Image/imori_gray.jpg', img_gray)
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
