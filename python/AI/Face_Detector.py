import cv2
import random

trainedFaceData = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
webcam = cv2.VideoCapture(0)
while (True):
    # capture frame and gray it
    successFrameRead, img = webcam.read()
    gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detect face and draw rectangles
    faceCoords = trainedFaceData.detectMultiScale(gImg)
    for (x, y, w, h) in faceCoords:
        cv2.rectangle(img, (x, y), (x + w, y + h), (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)), 2)

    # show output
    cv2.imshow("slaby face detector xd", img)
    key = cv2.waitKey(50)

    # exit
    if key == 81 or key == 113:
        break

print("code compleated")
