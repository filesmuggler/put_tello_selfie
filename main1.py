from djitellopy import Tello
import cv2
import time

from threading import Thread


def connect_to_wifi(self, ssid, password):
    """Connects to the Wi-Fi with SSID and password.
    After this command the tello will reboot.
    Only works with Tello EDUs.
    """
    return self.send_command_without_return('ap %s %s' % (ssid, password))

#arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
#arucoParams = cv2.aruco.DetectorParameters_create()

drone = Tello()
drone.connect()
#drone.streamon()

#frame_read = drone.get_frame_read()
drone.takeoff()
drone.move_down(30)
start = time.time()
diff = 0
#
# height, width, _ = frame_read.frame.shape
# video = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

while diff<30:
    temp = time.time()
    diff = temp - start
    # frame_read = drone.get_frame_read()
    # (corners, ids, rejected) = cv2.aruco.detectMarkers(frame_read.frame, arucoDict, parameters=arucoParams)
    # cv2.aruco.drawDetectedMarkers(frame_read.frame, corners, ids)
    # cv2.aruco.drawDetectedMarkers(frame_read.frame, rejected, borderColor=(100, 0, 240))
    # cv2.imshow('Live Video', frame_read.frame)
    # video.write(frame_read.frame)
    # cv2.waitKey(1)
    #
    # print(ids,rejected)

#video.release()

drone.land()
#drone.streamoff()
#cv2.destroyAllWindows()
drone.end()
#time.sleep(5)