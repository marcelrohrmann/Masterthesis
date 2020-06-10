import cv2

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,540)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)


#turn off autofocus
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)

focus = 85  # 187,170,153,136,119,102,85,68
cam.set(cv2.CAP_PROP_FOCUS, focus)

#print(cam.get(cv2.CAP_PROP_FOCUS))

cv2.namedWindow("stream")


img_counter = 0


while True:
    ret, frame = cam.read()
    cv2.imshow("stream", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k == ord('s'):
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        picture = cv2.imread(img_name, 1)
        cv2.imshow('win', picture)
        img_counter += 1
    if k== ord('p'):
        picture = cv2.imread('opencv_frame_0.png', 1)
        cv2.imshow('win', picture)


cam.release()


cv2.destroyAllWindows()