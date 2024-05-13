import cv2
import numpy as np

from scramble import *

ORANGE_MIN = np.array([0, 68, 170], np.uint8)
ORANGE_MAX = np.array([62, 217, 255], np.uint8)

# START: 
# Read image in color
img = cv2.imread("1131.jpg")

# Convert to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert to Gray
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
imgGray = cv2.inRange(imgHSV, ORANGE_MIN, ORANGE_MAX)

cv2.imshow('Gray', imgGray)

# FOR TESTING USE:
# Create a blank image
r,c = np.shape(imgGray)
blank = np.zeros([r,c])

# [Optional] Convert to Binary
imgBW = cv2.threshold(imgGray, 250, 255, cv2.THRESH_BINARY)[1]

# Edge detection
edgeImage = cv2.Canny(imgBW, 200, 255)

# FUNCTION CALL
# Send the binary edgeImage to scramble
# pix is number of pixels to randomly move the edge by
# thr is threshold to adjust minimum 'whiteness' of pixels if grayscale is used. [optional]
rows, cols = scramble(edgeImage, pix=15, thr=200)

## ALTERNATE: USE SCRAMBLE2
# rows, cols = scramble2(edgeImage, pix=15, thr=200)

# FOR TESTING USE
blank[rows, cols] = 255

# SHOW Unedited Edge
# cv2.imshow('Edge', cv2.bitwise_not(edgeImage))
cv2.imshow('Edge', edgeImage)

# SHOW Scrambled Edge
cv2.imshow('Scrambled', blank)

cv2.waitKey(0)
cv2.destroyAllWindows()