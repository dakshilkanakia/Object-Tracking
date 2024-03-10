import cv2
import numpy as np

def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LowHue','Tracking',0,255,nothing)
cv2.createTrackbar('LowSaturation','Tracking',0,255,nothing)
cv2.createTrackbar('LowValue','Tracking',0,255,nothing)
cv2.createTrackbar('UpperHue','Tracking',255,255,nothing)
cv2.createTrackbar('UpperSaturation','Tracking',255,255,nothing)
cv2.createTrackbar('UpperValue','Tracking',255,255,nothing)

while True:
	#frame = cv2.imread('rubberwhale2.png')
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lh = cv2.getTrackbarPos('LowHue','Tracking')
	ls = cv2.getTrackbarPos('LowSaturation','Tracking')
	lv = cv2.getTrackbarPos('LowValue','Tracking')

	uh = cv2.getTrackbarPos('UpperHue','Tracking')
	us = cv2.getTrackbarPos('UpperSaturation','Tracking')
	uv = cv2.getTrackbarPos('UpperValue','Tracking')


	lb = np.array([lh,ls,lv])
	ub = np.array([uh,us,uv])

	mask = cv2.inRange(hsv,lb,ub)

	res = cv2.bitwise_and(frame,frame,mask = mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	if (key := cv2.waitKey(1)) == 27:
		break

cap.release()
cv2.destroyAllWindows()
