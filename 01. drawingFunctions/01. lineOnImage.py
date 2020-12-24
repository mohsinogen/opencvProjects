#importing the opencv library
import cv2

#loading the image
myImage = cv2.imread('image.jpg')

#adding a diagonal on the image
editedImage = cv2.line(myImage, (0, 0), (640, 427), (255, 0, 0), 5)

#displaying the image
cv2.imshow('edited image', editedImage)
cv2.waitKey(0)