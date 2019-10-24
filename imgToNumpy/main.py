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

x = cv2.imread("sample.png", 0)
print(x)
#Indexing and slicing
print("\nIndexing and slicing Numpy array")
print("\n 1st Two rows in Numpy array")
print(x[0:2])
print("\n 2nd and 3rd indexed element in 1st Two rows in Numpy array")
print(x[0:2, 2:4])

print(x[:, 2:4])
print("\n Specific one element in numpy array")
print(x[1,3])

#Iterating Numpy Array
print("\nIterating Numpy Array")
print("\nIterating by Rows of Numpy array")
for i in x:
    print (i)
print("\nIterating by Columns of Numpy array")
for i in x.T:
    print (i)
print("\nIterating value by value")
for i in x.flat:
    print (i)