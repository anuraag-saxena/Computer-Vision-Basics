# Resizing and Cropping
import cv2

img = cv2.imread("Resources/img1.jpg")
# print(img.shape)  # img.shape[0]=>height, [1]=>width

# Resize
imgResize = cv2.resize(img, (300, 200))

# Cropping (used matrix)
imgCropped = img[0:200, 200:500]


# Display
cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)