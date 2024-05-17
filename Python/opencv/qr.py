import cv2
import numpy as np
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a = data
        break

cv2.imshow("QR code scanner", img)
webbrowser.open(str(a))


cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()