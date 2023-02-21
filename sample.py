import cv2

img = cv2.imread('image/press.png')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

trim_img = img[0:100, 0:100]
cv2.imshow('image', trim_img)
cv2.waitKey(0)
cv2.destroyAllWindows()