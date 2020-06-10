import numpy as np
import cv2

mtx = np.load('cameramatrix.npy')
dist = np.load('distortion_coefficients.npy')


img = cv2.imread('opencv_frame_5.png')
h,  w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.jpg',dst)