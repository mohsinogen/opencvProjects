#importing the opencv library
import cv2
import numpy as np

#loading the image
myImage = cv2.imread('image.jpg')

#adding a text on the image
editedImage = cv2.putText(myImage, 'Hello World', (138, 336), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

#displaying the image
cv2.imshow('edited image', editedImage)
cv2.waitKey(0)