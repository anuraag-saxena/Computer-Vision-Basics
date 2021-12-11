# draw shapes and texts
import cv2
import numpy as np

# colors
green       = (0, 255, 0)
red         = (0, 0, 255)
lightBlue   = (255, 255, 0)
darkGreen   = (0, 150, 0)


# an image with black color
img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255, 0, 0  # blue (whole image)


# create line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), green, 3)
# create rectangle
cv2.rectangle(img, (0,0), (250, 350), red, 2)
# for filled rectangle
cv2.rectangle(img, (250, 350), (350, 450), red, cv2.FILLED)
# create circle
cv2.circle(img, (400, 50), 30, lightBlue, 5)
# display text
cv2.putText(img, "OpenCV ", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, darkGreen, 3)


# Display Images
cv2.imshow("Image", img)

cv2.waitKey(0)
