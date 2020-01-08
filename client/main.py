import cv2
import numpy as np
#import socket

address = '' #change to address
port = 0; #change to port number

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, port))

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1000:
           s.send(b'0')
            continue
        s.send(b'1')
        cv2.rectangle(frame1, (x,y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Detecting Movement".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


    cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    cv2.imshow("feed", frame1)
    frame1= frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
s.close()
