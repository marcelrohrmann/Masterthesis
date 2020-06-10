import cv2
import numpy as np

#for stream with text
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)


#turn off autofocus
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)


focus = 85  # 187,170,153,136,119,102,85,68
cam.set(cv2.CAP_PROP_FOCUS, focus)


#print(cam.get(cv2.CAP_PROP_FOCUS))

img_counter = 0



while True:
    ret, stream_cam = cam.read()

    cv2.imshow("Stream ", stream_cam)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == ord('s'):
        # SPACE pressed
        img_name = "CameraCalibration_{}.png".format(img_counter)
        cv2.imwrite(img_name, stream_cam)
        print("{} written!".format(img_name))
        picture = cv2.imread(img_name, 1)
        cv2.imshow('saved picture', picture)
        img_counter += 1


cam.release()
cv2.destroyAllWindows()

