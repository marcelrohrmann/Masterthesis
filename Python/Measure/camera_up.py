import cv2

video = cv2.VideoCapture(1,cv2.CAP_DSHOW)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    connected, frame = video.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord('s'):
        video.release()
        break

cv2.destroyAllWindows()