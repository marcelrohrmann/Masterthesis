import cv2

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

r, frame = cap.read()


print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))