from keras.models import load_model
import cv2
import numpy as np

model = load_model('mode.h5')

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

img = cv2.imread('barackObama/test/img/1.jpg')
img = cv2.resize(img,(224,224))
img = np.reshape(img,[1,224,224,3])

classes = model.predict_classes(img)

print(classes)
