import time
import cv2
import numpy as np
from djitellopy import Tello

from tracker import Tracker

matrix_coefficients = np.array(
    [[929.562627, 0.000000, 487.474037], [0.000000, 928.604856, 363.165223], [0.000000, 0.000000, 1.000000]])
distortion_coefficients = np.array([-0.016272, 0.093492, 0.000093, 0.002999, 0.000000])

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
arucoParams = cv2.aruco.DetectorParameters_create()

drone = Tello()
drone.connect()
drone.takeoff()
drone.move_down(20)
drone.streamon()

frame_read = drone.get_frame_read()

start = time.time()
diff = 0
id_global = 18

height, width, _ = frame_read.frame.shape
video = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

pi_controllers = {
    'pi_x': [150, 150],
    'pi_y': [200, 150],
    'pi_d': [120, 120]
}

distance = 0.60

tracker = Tracker(width, height, distance, pi_controllers['pi_x'], pi_controllers['pi_y'], pi_controllers['pi_d'])

while diff < 60:
    temp = time.time()
    diff = temp - start
    frame_read = drone.get_frame_read()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame_read.frame, arucoDict, parameters=arucoParams)

    rvec = None
    tvec = None
    markerPoints = None

    if np.all(ids is not None):  # If there are markers found by detector
        for i in range(0, len(ids)):  # Iterate in markers
            # Estimate pose of each marker and return the values rvec and tvec---different from camera coefficients
            #print(ids[i])
            if ids[i] == id_global:
                rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.05, matrix_coefficients,
                                                                           distortion_coefficients)
                tvec = np.squeeze(tvec)
                s_1, s_2, s_3 = tracker(tvec[0], tvec[1], tvec[2], 0)
                #print(rvec)
                #print(s_1,s_2,s_3)
                drone.send_rc_control(s_1, s_3, s_2, 0)
                #print(ids[i], "position:", tvec)

    cv2.imshow('Live Video', frame_read.frame)
    video.write(frame_read.frame)
    cv2.waitKey(1)
video.release()
drone.streamoff()
drone.land()
cv2.destroyAllWindows()
drone.end()
