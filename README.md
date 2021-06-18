# put_tello_selfie
DJI Tello selfie "stick" is the project about creating drone following the person in some distance. It can be used for recording purposes by professional performers and streamers. We based our idea in using ArUco Tags. We couldn't stress the idea better than picturing this like below.

![alt text](https://github.com/filesmuggler/put_tello_selfie/blob/main/docs/idea.jpg)

Simplified solution can be found in this repository and you can feel free to modify anyway you want.

## Installation
We recommend using Python 3 for the project.
Make sure you are using virtual environment in python so to keep your system interpreter intact.
The short tutorial how to do this is published in the documentation [here](https://docs.python.org/3/library/venv.html)
To run the project please install djitellopy and opencv library.

```bash
pip install djitellopy opencv-python
```
## Run

```bash
python3 main.py
```
Program is prepared to detect all tags but assumes naively that their size is equal to 5cm per side. Results can be seen bellow.
![alt text](https://github.com/filesmuggler/put_tello_selfie/blob/main/docs/tags.jpg)

Detected tag location can be visualized on the image as follows.
![alt text](https://github.com/filesmuggler/put_tello_selfie/blob/main/docs/detect.png)

## Control
We are using PID controller for keeping a user given distance from the tag. 
PID equation.  

![alt text](https://github.com/filesmuggler/put_tello_selfie/blob/main/docs/pid.png)

We tried implementing the algorithm with ROS framework but for some undiscovered reason it appeared too laggy for aruco detection.

## References
- Python documentation (https://docs.python.org/3/)
- ArUco generator (https://chev.me/arucogen/)
- OpenCV library (https://opencv.org/)
- ArUco detection using OpenCv (https://docs.opencv.org/3.2.0/d5/dae/tutorial_aruco_detection.html)
- ROS library for DJI Tello (http://wiki.ros.org/tello_driver)
- DJI TelloPy library (https://djitellopy.readthedocs.io/en/latest/)

