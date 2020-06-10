#from read_text_file import *
import cv2
import numpy as np
import ColorCheck

circle_color_number = 186
rectangle_color_number = 29

#Import image
image = cv2.imread('opencv_frame_0.png')

#in NX red = 186, green = 29
if circle_color_number == 186:

    red_result = ColorCheck.red(image)

else:
    print("Bauteil hat nicht die Farbe rot")

#in NX red = 186, green = 29
if rectangle_color_number == 29:

    green_result = ColorCheck.green(image)
else:
    print("Bauteil hat nicht die Farbe grün")

image = cv2.resize(image, (640, 360))

#cv2.imshow('image', image)
#cv2.imshow('green_result', green_result)
#cv2.imshow('red_result', red_result)

#shape = number of rows, columns, and channels (if the image is color)
blank_image = np.zeros(shape=[360, 640, 3], dtype=np.uint8)

hstack = np.hstack([image, green_result])
hstack1 = np.hstack([red_result, blank_image])
vstack = np.vstack([hstack, hstack1])

cv2.imwrite("green_result.png", green_result)
cv2.imwrite("red_result.png", red_result)

#show array of pictures
cv2.imshow('vstack', vstack)


cv2.waitKey(0)