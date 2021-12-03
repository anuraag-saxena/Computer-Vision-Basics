import cv2

# ## Read Images/Video
# img = cv2.imread("Resources/img1.jpg")
# ## Display
# cv2.imshow("Output", img)
# cv2.waitKey(0) ## infintite delay


# ## Import video
# cap = cv2.VideoCapture("<video path>")
# while(True):
#     success, img = cap.read()
#     cv2.imshow("Imported video", img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break


## Using webcam
cap = cv2.VideoCapture(0)   #can be 1 or other, depending on you
cap.set(3, 640)     # width
cap.set(4, 480)     # height
cap.set(10, 100)    # brightness

while(True):
    success, img = cap.read()
    img = cv2.flip(img, 1)  # mirror image
    cv2.imshow("Imported video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

