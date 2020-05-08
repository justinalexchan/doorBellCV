import numpy as np 
import keras 
from keras import backend as K
from keras.models import Sequential 
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from keras.engine import InputLayer
from matplotlib import pyplot as pyplot
from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt 

train_path = 'NameOfPerson/train'
valid_path = 'NameOfPerson/valid'

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(224, 224), classes=['NameOfPerson', 'Unknown'], batch_size = 10)

# imports vgg16 model 
vgg16_model = keras.applications.vgg16.VGG16()

# "converts" the vgg16 functional model to sequential
model = Sequential()
model.add(InputLayer(input_shape=(224,224,3)))  

# removes the final layer with 1000 units
for layer in vgg16_model.layers[:-1]:
    model.add(layer)

for layer in model.layers:
    layer.trainable = False #freeze model/ prevent layers weights from being updated

# adds a final layer with 2 units
model.add(Dense(2, activation='softmax'))

model.compile(Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=15, validation_data = valid_batches, validation_steps=1, epochs=10, verbose=2)

model.save('model.h5')
