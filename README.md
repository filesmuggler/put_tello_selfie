# put_tello_selfie
DJI Tello selfie "stick" is the project about creating drone following the person in some distance. It can be used for recording purposes by professional performers and streamers. We based our idea in using ArUco Tags. We couldn't stress the idea better than picturing this like below.

![alt text](https://github.com/filesmuggler/put_tello_selfie/blob/main/docs/idea.jpg" 

Simplified solution can be found in this repository and you can feel free to modify anyway you want.

## Installation
We recommend using Python 3 for the project
Make sure you are using virtual environment in python so to keep your system interpreter intact.
The short tutorial how to do this is published in the documentation [here](https://docs.python.org/3/library/venv.html)
Install pytello and opencv library.

```bash
pip install pytello opencv-python
```
## Run

## Known Issues
As fas as we are proud to create such a fun project, we have to admit, that we still miss some things:

- [x] Pytello installation and Drone connectivity test
- [x] Retrieving image from camera and recording it
- [x] Detecting Aruco Tags with proper distance estimation using OpenCV 
- [ ] PID controller for keeping the distance

We tried implementing the algorithm with ROS framework but for some undiscovered reason it appeared too laggy for aruco detection.

## References


