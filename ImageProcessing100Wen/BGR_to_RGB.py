import cv2
print('OpenCV version:', cv2.__version__)
# function: BGR --> RGB

def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img

img = cv2.imread('./Image/imori.jpg')
img = BGR2RGB(img)
cv2.imwrite('./Image/imori_write.jpg', img)
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
