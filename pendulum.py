import cv2
import numpy as np

cap = cv2.VideoCapture('GOPR0173(1).avi')

while True:
	ret, frame1 = cap.read()
	
	#grayImage1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	
	ret, frame2 = cap.read()
	#grayImage2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	#diffImage = cv2.absdiff(grayImage1, grayImage2)
	diffImage = cv2.absdiff(frame1, frame2)
	retral, threshold = cv2.threshold(diffImage, 12, 255, cv2.THRESH_BINARY)
	grayImage = cv2.cvtColor(threshold, cv2.COLOR_BGR2GRAY)
	
	kernel = np.ones((15,15), np.float32) / 225
	smoothed = cv2.filter2D(grayImage, -1 , kernel)

	blur = cv2.GaussianBlur(grayImage, (15,15), 0)
	retral2, final = cv2.threshold(blur, 12, 255, cv2.THRESH_BINARY)
	
	cv2.imshow('frame',final)
	th, contours, hierarchy = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	
	if len(contours) > 0 & len(contours) < 10:
		point = cv2.boundingRect(contours[-1])
		x = (point[0] + point[1])/2
		y = (point[2] + point[3])/2
		if (x>300 & y>200) :
			print x
			print y
		
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
