######## Webcam Object Detection Using Tensorflow-trained Classifier #########
#
# Author: Evan Juras
# Date: 1/20/18
# Description:
# This program uses a TensorFlow-trained classifier to perform object detection.
# It loads the classifier and uses it to perform object detection on a webcam feed.
# It draws boxes, scores, and labels around the objects of interest in each frame
# from the webcam.

## Some of the code is copied from Google's example at
## https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

## and some is copied from Dat Tran's example at
## https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

## but I changed it to make it more understandable to me.


# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import time
counter = 0

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'

# Grab path to current working directory
#CWD_PATH = os.getcwd()
CWD_PATH = 'C:/tensorflow1/models/research/object_detection'

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph2.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap2.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 1

## Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Initialize webcam feed
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

#ret = video.set(3,1280)
#ret = video.set(4,720)

while True:

    # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    ret, frame = video.read()
    frame_expanded = np.expand_dims(frame, axis=0)

    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    # Draw the results of the detection (aka 'visulaize the results')
    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    # prints objects if score over 0.9

    objects = []
    threshold = 0.9



    #index 0 müsste cubesat-module sein
    for index, value in enumerate(classes[0]):
        object_dict = {}
        if scores[0, index] > threshold:
            object_dict[(category_index.get(value)).get('name').encode('utf8')] = scores[0, index]
            objects.insert(index, object_dict)


    print(objects)
    print(counter)


    # for i, b in enumerate(boxes[0]):
    #     if classes[0][i] == 1:
    #         if scores[0][i] >= 0.9:
    #             print(scores[0][i])

    # All the results have been drawn on the frame, so it's time to display it.
    cv2.imshow('Object detector', frame)

    if scores[0, 0] > threshold:
        print('Cubesat counter +1')
        counter = counter + 1

    if counter > 10:
        print('Cubesat detected 10 times, continue Quality Control')
        break

    # Press 'c' to quit
    if cv2.waitKey(1) == ord('c'):
        break

# Clean up
video.release()
cv2.destroyAllWindows()

cubesat_detected = cv2.imread('CubeSat detected.jpg')
cv2.imshow('cubesat_detected', cubesat_detected)

# waits 2 sec, shows image
cv2.waitKey(2000)
cv2.destroyAllWindows()


#after objectdetection start webcam test
import webcam
webcam.myfunc()

#Run color check with c
import ColorCheck
import keyboard

press_c = cv2.imread('PressCpic.jpg')
cv2.imshow('Continue press button', press_c)
cv2.waitKey(0)


#run color check

while True:
    if keyboard.is_pressed('c'):
        cv2.destroyWindow('Continue press button')
        ColorCheck.myfunc()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        break


print('next object measurement')
import object_size
object_size.myfunc()

print('next show all measurements')
import object_size_all
object_size_all.myfunc()

print('next show changed textfile')



import control4
control4.myfunc()

#robot control finished
print('robot control finished')