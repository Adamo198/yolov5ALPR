#!/usr/bin/env python3

import cv2
rtsp_username = ""
rtsp_password = ""
width = 800
height = 480

def create_camera(channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@0.0.0.0:554/cam/realmonitor?channel=" + str(channel) + "&subtype=1"
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 640)  # ID number for width is 3
    cap.set(4, 480)  # ID number for height is 4
    cap.set(10, 100)  # ID number for brightness is 10
    return cap

cam = create_camera(1)

while(True):
    success, frame = cam.read()
    dim = (width, height)
    full_frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)       
    cv2.imshow('screen', full_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
