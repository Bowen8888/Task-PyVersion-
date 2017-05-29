import cv2
import numpy as np
import sys

filename = sys.argv[1]

cap = cv2.VideoCapture(filename)
timeCount = 0
trial = 1
frame = 0
x=0
y=0
while True:
	ret, frame1 = cap.read()
	ret, frame2 = cap.read()

	diffImage = cv2.absdiff(frame1, frame2)
	retral, threshold = cv2.threshold(diffImage, 20, 21, cv2.THRESH_BINARY)
	grayImage = cv2.cvtColor(threshold, cv2.COLOR_BGR2GRAY)
	
	kernel = np.ones((15,15), np.float32) / 225
	smoothed = cv2.filter2D(grayImage, -1 , kernel)

	blur = cv2.GaussianBlur(grayImage, (15,15), 0)
	retral2, final = cv2.threshold(blur, 12, 255, cv2.THRESH_BINARY)
	
	cv2.imshow('Threshold of Blur',final)
	(contours, hierarchy) = cv2.findContours(final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	if len(contours) > 0 and len(contours) < 6 :
		
		point = cv2.boundingRect(contours[-1])
		
		timeCount = 0
		frame = frame + 1
		x = point[0]
		y = point[1]
		print 'trial: '+ str(trial)+ ' frame: ' + str(frame) + ' x: ' + str(point[0]) +' y: ' + str(point[1]) + ' ' + filename
			
			
		
	elif (timeCount > 20 and frame > 100):
		timeCount = 0
		frame = 0
		trial = trial +1
	else :
		
		timeCount = timeCount+1
		frame = frame + 1
		print 'trial: '+ str(trial)+ ' frame: ' + str(frame) + ' x: ' + str(x) +' y: ' + str(y) + ' ' + filename

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
