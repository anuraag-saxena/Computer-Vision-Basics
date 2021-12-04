# Basic Functions
import cv2
import numpy as np

img = cv2.imread("Resources/img1.jpg")
# kernel - a matrix needed for dilation
kernel = np.ones((5, 5), np.uint8)


# Functions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur - has to be odd no (3,3),(5,5)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# Edge Detector - Canny (to reduce edges increase threshold)
imgCanny = cv2.Canny(img, 150, 200)
# increase thickness of edge - Dialation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# opposite of dilation - erosion - make thinner
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


# Display Images
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
