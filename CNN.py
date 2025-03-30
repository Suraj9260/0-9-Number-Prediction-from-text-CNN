# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17ySiXJmVvg0w37KgdvKILAYRiXZItxbm
"""

import tensorflow as tf

mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_test.shape

x_train.shape

import matplotlib.pyplot as plt

#plt.imshow(x_train[0],cmap=plt.cm.binary)

#print(x_train[0])

x_train=tf.keras.utils.normalize(x_train)

x_test=tf.keras.utils.normalize(x_test)

#plt.imshow(x_train[0],cmap=plt.cm.binary)

import numpy as np
IMG_SIZE=28
x_train=np.array(x_train).reshape(-1,IMG_SIZE,IMG_SIZE,1)
x_test=np.array(x_test).reshape(-1,IMG_SIZE,IMG_SIZE,1)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D

model=Sequential()
#1st layer
model.add(Conv2D(64,(3,3),input_shape=x_train.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))


#2nd layer
model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#3rd layer
model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

#1st layer connection
model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))

#2nd layer connection
model.add(Dense(32))
model.add(Activation("relu"))

#3rd layer
model.add(Dense(10))
model.add(Activation("softmax"))

#model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam",metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10,validation_split=0.3)

test_loss,test_acc=model.evaluate(x_test,y_test)

predicion=model.predict(x_test)

print(np.argmax(predicion[9]))

plt.imshow(x_test[9])

imgtest=["/content/t1.png","/content/t2.png","/content/t3.png","/content/t4.png","/content/t5.png","/content/t6.png","/content/t7.png"]

def preprocess_and_predict(img_path):
    # Read the image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to 28x28 pixels
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    # Normalize the image
    img = tf.keras.utils.normalize(img, axis=1)

    # Reshape the image to fit the model input
    img = np.array(img).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    # Predict the image
    prediction = model.predict(img)

    return np.argmax(prediction)

# Plotting the images with predictions
plt.figure(figsize=(10, 10))
for i, img_path in enumerate(imgtest):
    plt.subplot(4, 4, i+1)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    prediction = preprocess_and_predict(img_path)
    plt.imshow(img, cmap='gray')
    plt.title(f'Predicted: {prediction}')
    plt.axis('off')

plt.tight_layout()
plt.show()

