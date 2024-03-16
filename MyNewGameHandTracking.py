import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
pTime = 0
cap = cv2.VideoCapture(1)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img, results = detector.findHands(img)
    # lmList = detector.findPosition(img)
    # if lmList:
    #     print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)),(10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
    cv2.putText(img, f'FPS:{int(fps)}', (480, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)