import cv2
import numpy as np


#1.1:BASICS

#In Color
#image = cv2.imread("Res/rocket.jpg")
#print(image.shape)

#grayscale
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print(gray.shape)

#HSV Image
#HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#print(HSV.shape)
#cv2.imshow("HSv", HSV)

#2.1:EDGE DETECTION

#image = cv2.imread("/home/eodin/Desktop/Kod/python/opencv/Res/rocket.jpg")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cannyImage = cv2.Canny(gray, 150, 300)
#cv2.imshow("Canny", cannyImage)

#2.2:Erosion and Dilation

#kernel = np.ones((3,3), np.uint8)
#dilated = cv2.dilate(cannyImage, kernel, iterations=1)
#erode_image = cv2.erode(dilated, kernel, iterations=1)
#cv2.imshow("Dilated", dilated)
#cv2.imshow("Eroded", erode_image)


#3.1:IMAGE MANIPULATION

#kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#image = cv2.imread("/home/eodin/Desktop/Kod/python/opencv/Res/noise.jpg")
#cv2.imshow("Noisy", image)
#sharp = cv2.filter2D(image, -1, kernel)
#cv2.imshow("Sharpened", sharp)
#dst = cv2.fastNlMeansDenoisingColored(sharp, None, 100, 80, 100, 8)
#cv2.imshow("DeNoised", dst)

#4.1:FACE DETECTION

#image = cv2.imread("Res/group3.jpg")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#faces = cascade.detectMultiScale(gray, 1.1, 4)
#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#cv2.imshow("Detected faces?", image)

#4.2:READING VIDEO

#cap = cv2.VideoCapture("Res/walking.mp4")
#while True:
#    ret, frame = cap.read()
#
#    if not ret:
#        break
#
#    cv2.imshow("Frame", frame)
#
#    key = cv2.waitKey(1)
#    if key == ord("q"):
#        break
#cap.release()
#cv2.destroyAllWindows()

#4.3:DISPLAYING VIDEO STREAM (cam)

#cap = cv2.VideoCapture(0)
#while True:
#    ret, frame =  cap.read()
#    cv2.imshow("Frame", frame)
#    if cv2.waitKey(1) == ord("q"):
#        break
#cap.release()
#cv2.destroyAllWindows()

#4.4:ADDING VIDEO EFFECTS

#cap = cv2.VideoCapture("Res/lavalamp.mp4")
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    height, width = frame.shape[:2]
#    zeros = np.zeros((height, width), dtype=np.uint8)
#    green = cv2.merge((zeros, gray, zeros))
#    cv2.imshow("Frame", green)
#    if cv2.waitKey(1) == ord("q"):
#        break
#cap.release()
#cv2.destroyAllWindows()


#4.5:VIDEO FACE DETECTION (cam)

#cap = cv2.VideoCapture(0)
#cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#while True:
#    _, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = cascade.detectMultiScale(gray, 1.1, 4)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#    cv2.imshow("RT Face Detection", frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#cap.release()
#cv2.destroyAllWindows()

#4.6:VIDEO FACE DETECTION (video) (very unstable if alot of movement)

#cap = cv2.VideoCapture("Res/towards.mp4")
#cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#while True:
#    _, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = cascade.detectMultiScale(gray, 1.1, 4)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#    cv2.imshow("RT Face Detection", frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#cap.release()
#cv2.destroyAllWindows()

#4.7:OBJECT TRACKING (template matching)

#cap = cv2.VideoCapture("Res/torg.mp4")
#ret, frame = cap.read()
#bbox = cv2.selectROI("Object", frame, False)
#template = frame[int(bbox[1]) : int(bbox[1] + bbox[3]), int(bbox[0]) : int(bbox[0] + bbox[2])]
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
#    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#    top_left = max_loc
#    bottom_right = (top_left[0] + int(bbox[2]), top_left[1] + int(bbox[3]))
#    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
#    cv2.imshow("Tracked Obj", frame)
#    if cv2.waitKey(30) & 0xff == 27:
#        break

#4.8:OBJECT TRACKING (Mean Shift) (cant take noise)

#cap = cv2.VideoCapture("Res/towards.mp4")
#ret, frame = cap.read()
#bbox = cv2.selectROI("Object", frame, False)
#x, y, w, h = bbox
#track_window = (x, y, w, h)
#term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#    roi = hsv[y:y + h, x:x + w]
#    roi_hist = cv2.calcHist([roi], [0], None, [180], [0, 180])
#    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
#    ret, track_window = cv2.meanShift(dst, track_window, term_crit)
#    x, y, w, h = track_window
#    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#    cv2.imshow("Tracked Object", frame)
#
#    k = cv2.waitKey(30) & 0xff
#    if k == 27:
#        break

#4.9 OBJECT TRACKING (Kalman Filtering)

#cap = cv2.VideoCapture("Res/torg.mp4")
#ret, frame = cap.read()
#bbox = cv2.selectROI("Object", frame, False)
#dt = 1 / 30.0
#A = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])
#B = np.zeros((4, 2))
#C = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
#Q = np.eye(4)*0.1
#R = np.eye(2)*10
#x = np.array([[bbox[0]], [bbox[1]], [0], [0]])
#P = np.eye(4)
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    x = A.dot(x) + B.dot(np.array([[np.random.normal()], [np.random.normal()]]))
#    P = A.dot(P).dot(A.T) + Q
#    z = np.array([[bbox[0]+bbox[2] / 2], [bbox[1]+bbox[3] / 2]])
#    y = z - C.dot(x)
#    S = C.dot(P).dot(C.T) + R
#    K = P.dot(C.T).dot(np.linalg.inv(S))
#    x = x + K.dot(y)
#    P = (np.eye(4) - K.dot(C)).dot(P) 
#    x_, y_, w_, h_ = map(int, [x[0, 0] - bbox[2] / 2, x[1, 0] - bbox[3] / 2, bbox[2], bbox[3]])
#    cv2.rectangle(frame, (x_, y_), (x_ + w_, y_ + h_), (0, 255, 0), 2)
#    cv2.imshow("Tracked Object", frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


# !TEST! OBJECT TRACKING IN STREAM (cam) (template matching) (kind of works... needs tweaking) 
# !TWO times on q to exit!

#cap = cv2.VideoCapture(0)
#ret, frame = cap.read()
#bbox = cv2.selectROI("Object", frame, False)
#template = frame[int(bbox[1]) : int(bbox[1] + bbox[3]), int(bbox[0]) : int(bbox[0] + bbox[2])]
#while True:
#    ret, frame = cap.read()
#    if not ret:
#        break
#    height, width, _ = frame.shape
#    scale_percent = 200
#    new_width = int(width * scale_percent / 100)
#    new_height = int(height * scale_percent /100)
#    dim = (new_width, new_height)
#    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
#    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#    top_left = max_loc
#    bottom_right = (top_left[0] + int(bbox[2]), top_left[1] + int(bbox[3]))
#    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
#    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
#    cv2.imshow("Tracked Obj", resized)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#5.1: MOTION ANALYSIS (basically optical motion detection)

#cap = cv2.VideoCapture("Res/torg.mp4")
#ret, frame = cap.read()
#fgbg = cv2.createBackgroundSubtractorMOG2()
#fgmask = fgbg.apply(frame)
#ret, frame1 = cap.read()
#prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
#mask = np.zeros_like(frame1)
#lk_params = dict(winSize = (15, 15),
#                 maxLevel = 4,
#                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
#while True:
#    ret, frame2 = cap.read()
#    if not ret:
#        break
#    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
#    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
#    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
#    mag_scaled = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
#    ang_degrees = ang * 180 / np.pi / 2
#    ang_scaled = cv2.normalize(ang_degrees, None, 0, 255, cv2.NORM_MINMAX)
#    hsv = np.zeros_like(frame1)
#    hsv[..., 0] = ang_scaled
#    hsv[..., 1] = 255
#    hsv[..., 2] = cv2.convertScaleAbs(mag_scaled)
#    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#    height, width, _ = bgr.shape
#    scale_percent = 75
#    new_width = int(width * scale_percent / 100)
#    new_height = int(height * scale_percent /100)
#   dim = (new_width, new_height)
#   resized = cv2.resize(bgr, dim, interpolation=cv2.INTER_AREA)
#    cv2.imshow("Optical Flow", resized)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#    prvs = next.copy()
#cap.release()
#cv2.destroyAllWindows()


#5.2:FEATURE TRACKING ( need tweaking)

cap = cv2.VideoCapture("Res/torg.mp4")
ret, frame = cap.read()
fgbg = cv2.createBackgroundSubtractorMOG2()
fgmask = fgbg.apply(frame)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_gray = gray.copy()
prevPts = cv2.goodFeaturesToTrack(prev_gray, maxCorners=200, qualityLevel=0.01, minDistance=30)
mask = np.zeros_like(frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, gray, prevPts, None)
    goodNew = nextPts[status == 1]
    goodOld = prevPts[status == 1]
    H, _ = cv2.findHomography(goodOld, goodNew, cv2.RANSAC, 3.0)
    h, w = frame.shape[:2]
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)
    img = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("Feature tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    prev_gray = gray.copy()
    prevPts = goodNew.reshape(-1, 1, 2)




#LEAVE WAITKEY UNCOMMENTED
cv2.waitKey(0)