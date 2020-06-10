from read_text_file import *
import cv2
import numpy as np


#check for red circle
image = cv2.imread('opencv_frame_0.png')

#convert to HSV
imgHsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#in NX red = 186, green = 29
if circle_color_number == 186:

    #HSV Filter Rot
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
    red_result = cv2.resize(red_result, (640, 360))

    cv2.imshow('red_result', red_result)

    redpoints = cv2.countNonZero(mask)

    if redpoints > 5000:
        print('Das Bauteil rot ist mit ' + str(redpoints) + ' Punkten vorhanden')
    else:
        print('Das Bauteil rot ist nicht vorhanden')

else:
    print("Bauteil hat nicht die Farbe rot")

if rectangle_color_number == 29:

    # HSV Filter Rot
    h_min = 50
    h_max = 100
    s_min = 60
    s_max = 255
    v_min = 70
    v_max = 250

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)

    green_result = cv2.bitwise_and(image, image, mask=mask)
    green_result = cv2.resize(green_result, (640, 360))


    cv2.imshow('green_result', green_result)


    redpoints = cv2.countNonZero(mask)

    if redpoints > 5000:
        print('Das Bauteil grün ist mit ' + str(redpoints) + ' Punkten vorhanden')
    else:
        print('Die Bauteil grün ist nicht vorhanden')

else:
    print("Bauteil hat nicht die Farbe grün")

image = cv2.resize(image, (640, 360))
cv2.imshow('image', image)
cv2.waitKey(0)