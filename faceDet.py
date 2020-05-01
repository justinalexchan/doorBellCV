import numpy as np
import cv2
import serial

seri = serial.Serial('COM3', 9600)

cap = cv2.VideoCapture(0)
while(True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#pathEyes = "haarcascade_eye_tree_eyeglasses.xml"
	pathFace = "haarcascade_frontalface_default.xml"
	#pathNose = "haarcascade_nose.xml"

	#eye_cascade = cv2.CascadeClassifier(pathEyes)
	face_cascade = cv2.CascadeClassifier(pathFace)
	#nose_cascade = cv2.CascadeClassifier(pathNose)

	#eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
	#nose = nose_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

	eyeDistance = 0
	xEye = 0
	yEye = 0
	initEye = 1
	eyeCoord = []

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		'''
		for (x, y, w, h) in eyes:
			cv2.circle(img, (x+int(w/2),y+int(h/2)), 10, (255,0,0), 1)
			eyeCoord.append(x+int(w/2))
			eyeCoord.append(y+int(h/2))
		for (x, y, w, h) in nose:
			cv2.circle(img, (x+int(w/2),y+int(h/2)), 10, (0,0,255), 1)
		'''


	#if len(eyes)>1:
	#	cv2.line(img, (eyeCoord[0],eyeCoord[1]), (eyeCoord[2], eyeCoord[3]), (255,0,0), 2)
	cv2.imshow("Image",img)
	ch = cv2.waitKey(1)
	
	if ch & 0xFF == ord('q'):
		break

	if len(faces) > 0:
		seri.write('1'.encode())
		print("1")
	else:
		seri.write('0'.encode())
		print("0")

	

cap.release()
cv2.destroyAllWindows()