# DoorBellCV 
DoorBellCV is a application that uses deep learning and computer vision to detect and determine whether or not a face was recognizable by a trained model. The program will then proceed to ring the doorbell or unlock the door. 

### Project Overview:
DoorBellCV captures video from a camera and parses it to determine if any human faces are in the frame. This is done with the help of OpenCV and a pretrained haar cascade classifier (haarcascade_frontalface_default.xml). This allows for faces to be detected while they are in motion. 



A CNN was the built using Kera, a deep learning framework for python. The VGG16 model was used and modified for to classfy specific faces. 

