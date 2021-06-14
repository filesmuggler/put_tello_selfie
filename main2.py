from djitellopy import Tello
import cv2
import time
import numpy as np

from threading import Thread

matrix_coefficients = np.array([[929.562627, 0.000000, 487.474037], [0.000000, 928.604856, 363.165223], [0.000000, 0.000000, 1.000000]])
distortion_coefficients = np.array([-0.016272, 0.093492, 0.000093, 0.002999, 0.000000])


arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()

drone = Tello()
drone.connect()
drone.streamon()

frame_read = drone.get_frame_read()

start = time.time()
diff = 0

height, width, _ = frame_read.frame.shape
video = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

while diff<40:
    temp = time.time()
    diff = temp - start
    frame_read = drone.get_frame_read()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame_read.frame, arucoDict, parameters=arucoParams)

    if np.all(ids is not None):  # If there are markers found by detector
        for i in range(0, len(ids)):  # Iterate in markers
            # Estimate pose of each marker and return the values rvec and tvec---different from camera coefficients
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.05, matrix_coefficients,
                                                                       distortion_coefficients)
            print(ids[i],"position:", tvec)

    cv2.imshow('Live Video', frame_read.frame)
    video.write(frame_read.frame)
    cv2.waitKey(1)


video.release()

drone.streamoff()
cv2.destroyAllWindows()
drone.end()