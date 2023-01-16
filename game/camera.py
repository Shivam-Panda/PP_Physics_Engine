import math

import cv2
import numpy as np
from data_reader import *

objects = []

k_constant = 500
contact_time = 1
mass = 1

cap = cv2.VideoCapture(0)


x_dists = []
global bow_height

_init = False
began = False

def find_mean_point(approx):
    x_vals = []
    y_vals = []
    for i in approx:
        x_vals.append(i[0][0])
        y_vals.append(i[0][1])
    return [sum(x_vals)/4, sum(y_vals)/4]

def nothing(x):
    pass

def shoot(x):
    set_data('SHOOT', True)

def init(x):
    global _init 
    _init = True
    
def average(l):
    return sum(l)/len(l)

def begin(x):
    global began
    began = True
    global _init
    _init = False


cv2.namedWindow('result')
cv2.createTrackbar('Shoot', 'result', 0, 1, shoot)
cv2.createTrackbar('Init', 'result', 0, 1, init)
cv2.createTrackbar('Begin', 'result', 0, 1, begin)

# cv2.createTrackbar('h_low', 'result', 0, 179, nothing)
# cv2.createTrackbar('s_low', 'result', 0, 255, nothing)
# cv2.createTrackbar('v_low', 'result', 0, 255, nothing)

# cv2.createTrackbar('h_upper', 'result', 0, 179, nothing)
# cv2.createTrackbar('s_upper', 'result', 0, 255, nothing)
# cv2.createTrackbar('v_upper', 'result', 0, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # h_low=  cv2.getTrackbarPos('h_low', 'result')
    # s_low=  cv2.getTrackbarPos('s_low', 'result')
    # v_low=  cv2.getTrackbarPos('v_low', 'result')

    # h_upper =  cv2.getTrackbarPos('h_upper', 'result')
    # s_upper =  cv2.getTrackbarPos('s_upper', 'result')
    # v_upper =  cv2.getTrackbarPos('v_upper', 'result')

    low_orange = np.array([20,52,116])
    high_orange = np.array([36,103,232])
    # # 
    # low_orange = np.array([h_low, s_low, v_low])
    # high_orange = np.array([h_upper, s_upper, v_upper])

    mask = cv2.inRange(hsv, low_orange, high_orange)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    points = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.05 * cv2.arcLength(cnt, True), True)
        if area > 400 and len(approx) == 4:
            points.append(find_mean_point(approx))
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

    if len(points) == 3 and _init:
        print(began)
        xs = []
        ys = []
        for i in points:
            xs.append(i[0])
            ys.append(i[1])
        bow_height = max(ys) - min(ys)
        j = ys.index(max(ys))
        xps = []
        for i in xs:
            if i == j:
                pass
            else:
                xps.append(i)
        x_dists.append(abs(xps[0]-xps[1]))
    elif len(points) == 2 and len(x_dists) >= 10 and began:
        x_points = []
        y_points = []
        for i in points:
            x_points.append(i[0])
            y_points.append(i[1])
        x_dist = abs(x_points[0]-x_points[1])
        y_dist = (y_points[0]-y_points[1])

        y_angle = math.atan(y_dist/x_dist)
        print(math.degrees(y_angle))

        x_more = abs((average(x_dists) - x_dist))
        
        F = k_constant*(math.sqrt(bow_height**2+x_more**2)-bow_height)*(math.cos(math.atan(bow_height/x_more)))
        velocity = (F*contact_time)/mass
        
        # set_data('XY_SLOPE', y_angle)
        # set_data('VELOCITY', velocity)
    else:
        pass

    # cv2.imshow('Frame', frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
