# importing the libraries
import cv2
import numpy as np

# function for sketch like effect
def sketch(image):
    #converting image to grayscale
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # adding blur effect
    imgGrayBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
    
    # extracting edges from the image
    cannyEdge = cv2.Canny(imgGrayBlur, 40, 90)

    #invert binarize
    ret, mask = cv2.threshold(cannyEdge, 90, 255, cv2.THRESH_BINARY_INV)

    return mask


#initializing webcam and calling our sketch function

cap = cv2.VideoCapture(0)  #you can enter any video file path too

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Sketch App', sketch(frame))

    if cv2.waitKey(1) == 13: # break loop when pressed enter
        break

cap.release()
cv2.destroyAllWindows()

