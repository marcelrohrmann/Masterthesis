import cv2
import numpy as np
import read_expression
# Read image.
img = cv2.imread('red_result.png', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=0, maxRadius=0)
print(detected_circles)
# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        print(a,b,r)

        pixelsPerMetric = 34/23
        r = r / pixelsPerMetric
        r = r.round(1)

        cv2.putText(img, 'radius= '+str(r)+'mm', (a+50,b), cv2.FONT_HERSHEY_SIMPLEX ,
                            fontScale= 0.5, color = (255, 255, 255), thickness = 2)
        cv2.putText(img, "NX size is: " + str(read_expression.diameter),
                    (a + 50, b+30), cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.65, color=(0, 0, 255), thickness=2)
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)