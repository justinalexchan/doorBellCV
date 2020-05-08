from keras.models import load_model
import cv2
import numpy as np
import serial

#Serial Com
seri = serial.Serial('COM3', 9600)

#Load trained model
model = load_model('obamaModel.h5')

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

#Sent characteristics of font
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,100)
fontScale = 1
fontColor = (255,0,0)
lineType = 2

#Set cv2 to use onboard camera
cap = cv2.VideoCapture(0)
while(True):
	ret, img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	pathFace = "haarcascade_frontalface_default.xml"
	face_cascade = cv2.CascadeClassifier(pathFace)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

	
	dimensions = []
	classes = 1
	rectArea = 0
	#Draw rectangle around detected face(s)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		dimensions.append(x)
		dimensions.append(y)
		dimensions.append(w)
		dimensions.append(h)
		rectArea = ((x - (x +w))**2 + (y - (y+h))**2)**(0.5)
		#print("x: " + str(x) +" y: " + str(y) + "w: " + str(w) +" h: " + str(h))	
		#print(rectArea)

	#If face is present, crop the face image and feed it into the trained model
	if len(dimensions) and  rectArea > 300:
		crop_img = img[dimensions[1]:dimensions[1]+dimensions[3], dimensions[0]:dimensions[0]+dimensions[2]]
		sampl = cv2.resize(img,(224,224))
		sampl = np.reshape(sampl,[1,224,224,3])
		classes = model.predict_classes(sampl)

		#Print face data to the screen
		if(classes == 0):
			cv2.putText(img,'Barack Obama', 
				bottomLeftCornerOfText, 
				font, 
				fontScale,
				fontColor,
				lineType)
		elif(classes == 1):
			cv2.putText(img,'Unknown', 
				bottomLeftCornerOfText, 
				font, 
				fontScale,
				fontColor,
				lineType)
	else:
		cv2.putText(img,'Come Closer', 
				bottomLeftCornerOfText, 
				font, 
				fontScale,
				(0,0,255),
				lineType)

	cv2.imshow("Image",img)
	ch = cv2.waitKey(1)
	
	if ch & 0xFF == ord('q'):
		break
	
	#Sends serial Data based on classification
	if len(faces) > 0 and classes == 0:
		seri.write('1'.encode())
	else:
		seri.write('0'.encode())

cap.release()
cv2.destroyAllWindows()