# warp perspective
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")


# for a particular card
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
# to wrap it to size
width, height = 250, 350
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# for perspective transform
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


# Display Images
cv2.imshow("Image", img)
cv2.imshow("Warp Perspective", imgOutput)

cv2.waitKey(0)

