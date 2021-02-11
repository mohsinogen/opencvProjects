#importing the opencv library
import cv2

#loading the image
myImage = cv2.imread('image.jpg')

#adding a diagonal on the image
editedImage = cv2.rectangle(myImage, (200,113), (400, 228), 4)


#displaying the image
cv2.imshow('edited image', editedImage)
cv2.waitKey(0)