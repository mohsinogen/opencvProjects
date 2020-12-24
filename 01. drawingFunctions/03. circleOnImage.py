#importing the opencv library
import cv2

#loading the image
myImage = cv2.imread('image.jpg')

#adding a circle on the image
editedImage = cv2.circle(myImage, (311, 170), 60, (255, 0, 0), 2)

#displaying the image
cv2.imshow('edited image', editedImage)
cv2.waitKey(0)