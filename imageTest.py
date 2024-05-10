import cv2
import numpy

from scramble import *

# START: 
# Read image in color
img = cv2.imread("SmallTriangle.png")

# Convert to Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# FOR TESTING USE:
# Create a blank image
r,c = np.shape(imgGray)
blank = numpy.ones([r,c])*255

# [Optional] Convert to Binary
imgBW = cv2.threshold(imgGray, 250, 255, cv2.THRESH_BINARY)[1]

# Edge detection
edgeImage = cv2.Canny(imgBW, 200, 255)

# FUNCTION CALL
# Send the binary edgeImage to scramble
# pix is number of pixels to randomly move the edge by
# thr is threshold to adjust minimum 'whiteness' of pixels if grayscale is used. [optional]
rows, cols = scramble(edgeImage, pix=15, thr=200)


# Copy the original RGB Image
# Set all channels to 255 at the Scrambled locations
scramImg = img.copy()
scramImg[rows, cols, :] = 255

# FOR TESTING USE
blank[rows, cols] = 0

# SHOW Unedited Edge
cv2.imshow('Edge', cv2.bitwise_not(edgeImage))

# SHOW Scrambled Edge
cv2.imshow('Scrambled', blank)

cv2.waitKey(0)
cv2.destroyAllWindows()