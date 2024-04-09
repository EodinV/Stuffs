import cv2 as c

print("Tada")

img = c.imread("Res/rocket.jpg") 
c.imshow("Not a raccoon", img)

c.waitKey(0)