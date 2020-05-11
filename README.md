# DoorBellCV 
DoorBellCV is a application that uses deep learning and computer vision to detect and determine whether or not a face was recognizable by a trained model. The program will then proceed to ring the doorbell or unlock the door. 

### Project Overview:

#### Facial Detection and Recognition
DoorBellCV captures video from a camera and parses it to determine if any human faces are in the frame. This is done with the help of OpenCV and a pretrained haar cascade classifier (haarcascade_frontalface_default.xml). This allows for faces to be detected while they are in motion. 

The following is the face detection algorithm working on a video of steve jobs (iPhone presentation 2007):

<p align="center">
   <img src=https://github.com/justinalexchan/doorBellCV/blob/master/imagesVideos/steveJobsDemo.gif alt="FaceDetDemo" width="300" height="300">  <img src=https://github.com/justinalexchan/doorBellCV/blob/master/imagesVideos/recognition.gif alt="FaceRecognition" width="300" height="300"> 
</p>

A CNN was the built using Kera, a deep learning framework for python. The VGG16 model was used and modified for to classfy specific faces. An example model was trained to recognize the face of Barack Obama. The model was trained with 100 images (50 of the target and 50 of random faces) and was validated with another 50 images.


An addition adjustment was made so that a person must be within a certain distance of the camera in order for recognition to begin. This was done to reduce the frequncy of false positives.

<p align="center">
   <img src=https://github.com/justinalexchan/doorBellCV/blob/master/imagesVideos/outOfRange.gif alt="FaceOutOfRange" width="300" height="300"> 
</p>

