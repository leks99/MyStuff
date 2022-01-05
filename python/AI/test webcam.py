import cv2

webcam = cv2.VideoCapture(0)

while (True):
    successFrameRead, frame = webcam.read()
    cv2.imshow("test", frame)
    break
