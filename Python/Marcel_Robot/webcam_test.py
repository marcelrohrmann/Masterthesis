import cv2
import numpy as np

#for stream with text
cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

#for saving picture without text
cam2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cam2.set(cv2.CAP_PROP_FRAME_WIDTH,1280)

#turn off autofocus
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cam2.set(cv2.CAP_PROP_AUTOFOCUS, 0)

focus = 85  # 187,170,153,136,119,102,85,68
cam.set(cv2.CAP_PROP_FOCUS, focus)
cam2.set(cv2.CAP_PROP_FOCUS, focus)

#print(cam.get(cv2.CAP_PROP_FOCUS))

img_counter = 0



while True:
    ret, stream_cam = cam.read()
    ret, save_cam = cam2.read()
    #put text on stream_cam
    cv2.putText(stream_cam, "ESC = Close", (20, 650), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 0, 0), thickness=3)
    cv2.putText(stream_cam, "S = Save Picture", (20, 700), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 0, 0), thickness=3)
    cv2.imshow("Stream Quality Control", stream_cam)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == ord('s'):
        # SPACE pressed
        img_name = "cubesat_picture_{}.png".format(img_counter)
        cv2.imwrite(img_name, save_cam)
        print("{} written!".format(img_name))
        picture = cv2.imread(img_name, 1)
        cv2.imshow('saved picture', picture)
        img_counter += 1


cam.release()
cv2.destroyAllWindows()