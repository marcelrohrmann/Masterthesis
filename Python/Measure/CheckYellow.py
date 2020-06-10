import cv2
import numpy as np

image = cv2.imread('opencv_frame_0.png')
#convert to HSV
imgHsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#grün: H=40..100, S=60..255, V=70..250
#green color
h_min = 50
h_max = 100
s_min = 60
s_max = 255
v_min = 70
v_max = 250

lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])

mask = cv2.inRange(imgHsv, lower, upper)
yellow_result = cv2.bitwise_and(image,image, mask = mask)
cv2.imshow('result', yellow_result)

anzahl = cv2.countNonZero(mask)

if anzahl > 1000:
    print('Die Farbe grün ist ' + str(anzahl) + ' Punkten vorhanden')
else:
    print('Die farbe gelb ist nicht ausreichend vorhanden')

# rot: H=0..20, S= 130..255, V= 0..255

#Rot
h_min = 0
h_max = 20
s_min = 130
s_max = 255
v_min = 0
v_max = 255

lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])
mask = cv2.inRange(imgHsv, lower, upper)

red_result = cv2.bitwise_and(image,image, mask = mask)
cv2.imshow("mask", yellow_result)
cv2.imshow('result', red_result)
cv2.imshow('image',image)

redpoints = cv2.countNonZero(mask)

if redpoints > 1000:
    print('Die Farbe rot ist mit ' + str(redpoints) + ' Punkten vorhanden')
else:
    print('Die farbe gelb ist nicht ausreichend vorhanden')

cv2.waitKey(0)