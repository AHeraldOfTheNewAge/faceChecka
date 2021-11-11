#https://towardsdatascience.com/object-detection-with-tensorflow-model-and-opencv-d839f3e42849
#use cpu lol
#https://stackoverflow.com/questions/59499764/tensorflow-not-tensorflow-gpu-failed-call-to-cuinit-unknown-error-303

import tensorflow_hub as hub
import cv2
import numpy
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import json
import tensorflow_text

width = 1028
height = 1028

#Load image by Opencv2
img = cv2.imread('image.jpg')
#Resize to respect the input_shape
inp = cv2.resize(img, (width , height ))

#Convert img to RGB
rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)

# COnverting to uint8
rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

#Add dims to rgb_tensor
rgb_tensor = tf.expand_dims(rgb_tensor , 0)

# print(rgb_tensor)

# Loading model directly from TensorFlow Hub
detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

# Loading csv with labels of classes
labels = pd.read_csv('labels.csv', sep=';', index_col='ID')
labels = labels['OBJECT (2017 REL.)']

# Creating prediction
boxes, scores, classes, num_detections = detector(rgb_tensor)

# Processing outputs
pred_labels = classes.numpy().astype('int')[0]
pred_labels = [labels[i] for i in pred_labels]
pred_boxes = boxes.numpy()[0].astype('int')
pred_scores = scores.numpy()[0]

resultArr = []

# Putting the boxes and labels on the image
for score, label in zip(pred_scores, pred_labels):
    if score < 0.5:
        continue
    #de facut pe 0.4 ?o

    resultArr.append([label, str(score)[:4]])
    #we convert float32 to string + we only keep the first 4 characters
    #because we dont need to store that much of a confidence rate

print(json.dumps(resultArr))



#
