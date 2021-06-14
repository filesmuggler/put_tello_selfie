from djitellopy import Tello
import cv2
import time
import numpy as np

from threading import Thread

matrix_coefficients = np.array([[929.562627, 0.000000, 487.474037], [0.000000, 928.604856, 363.165223], [0.000000, 0.000000, 1.000000]])
distortion_coefficients = np.array([-0.016272, 0.093492, 0.000093, 0.002999, 0.000000])

def connect_to_wifi(self, ssid, password):
    """Connects to the Wi-Fi with SSID and password.
    After this command the tello will reboot.
    Only works with Tello EDUs.
    """
    return self.send_command_without_return('ap %s %s' % (ssid, password))

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
            (rvec - tvec).any()  # get rid of that nasty numpy value array error

            #cv2.aruco.drawDetectedMarkers(frame_read.frame, corners, ids)
            cv2.aruco.drawDetectedMarkers(frame_read.frame, rejected, borderColor=(100, 0, 240))
            cv2.aruco.drawAxis(frame_read.frame, matrix_coefficients, distortion_coefficients, rvec, tvec,0.01)  # Draw Axis

            print(ids[i],"position:", tvec)
    cv2.imshow('Live Video', frame_read.frame)
    video.write(frame_read.frame)
    cv2.waitKey(1)

    #print(ids,rejected)


video.release()

drone.streamoff()
cv2.destroyAllWindows()
drone.end()
#time.sleep(5)