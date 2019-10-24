import cv2
import numpy
# reading image in grey scale
img_num1 = cv2.imread("mario.png", 0)
print(img_num1)
# reading image in BGR 
img_num2 = cv2.imread("mario.png", 1)
print(img_num2)
# creating images out of an Numpy array
cv2.imwrite("new-mario1.png", img_num1)
cv2.imwrite("new-mario2.png", img_num2)