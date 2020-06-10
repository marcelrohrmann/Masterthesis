def myfunc():
    import cv2
    import numpy as np
    import read_expression
    # import data from read_expression
    print('hello')
    image = cv2.imread('cubesat_picture_0.png')

    # convert to HSV
    imgHsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Boolean for Color Check Processes
    red_check_succesfull = False
    green_check_succesfull = False

    # grün: H=40..100, S=60..255, V=70..250
    # green color
    if read_expression.rectangle_color_number == 29:
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

        greenpoints = cv2.countNonZero(mask)

        if greenpoints > 5000:
            print('Die Farbe grün ist ' + str(greenpoints) + ' Punkten vorhanden')
            green_check_succesfull = True
        else:
            print('Die farbe gelb ist nicht ausreichend vorhanden')
    else:
        print('NX Color has changed. Is not yet defined')
        green_result = np.zeros(shape=[360, 640, 3], dtype=np.uint8)
        cv2.putText(green_result, "NX Color has changed. Not defined", (20, 180), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 0, 255), thickness=2)

    # rot: H=0..20, S= 130..255, V= 0..255
    if read_expression.circle_color_number == 186:
        h_min = 0
        h_max = 20
        s_min = 130
        s_max = 255
        v_min = 0
        v_max = 255

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHsv, lower, upper)

        red_result = cv2.bitwise_and(image, image, mask=mask)
        red_result = cv2.resize(red_result, (640, 360))

        redpoints = cv2.countNonZero(mask)

        if redpoints > 5000:
            print('Die Farbe rot ist mit ' + str(redpoints) + ' Punkten vorhanden')
            red_check_succesfull = True
        else:
            print('Das Bauteil rot ist nicht vorhanden')
    else:
        print('NX Color has changed. Is not yet defined')
        red_result = np.zeros(shape=[360, 640, 3], dtype=np.uint8)
        cv2.putText(red_result, "NX Color has changed. Not defined", (20, 180), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 0, 255), thickness=2)

    image = cv2.resize(image, (640, 360))

    # shape = number of rows, columns, and channels (if the image is color)
    blank_image = np.zeros(shape=[360, 640, 3], dtype=np.uint8)

    # check if green, red check was succesfull
    if green_check_succesfull == True and red_check_succesfull == True:
        cv2.putText(blank_image, "Checks sucessfull", (120, 180), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 0, 255), thickness=2)

    hstack = np.hstack([image, green_result])
    hstack1 = np.hstack([red_result, blank_image])
    vstack = np.vstack([hstack, hstack1])

    cv2.imwrite("green_result.png", green_result)
    cv2.imwrite("red_result.png", red_result)

    # show array of pictures
    cv2.imshow('vstack', vstack)

    cv2.waitKey(0)
