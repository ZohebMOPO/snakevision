import numpy as np
import cv2
import pyautogui
from directKeys import up, left, down, right
from directKeys import PressKey, ReleaseKey

blueLower = np.array([50, 50, 50])
blueUpper = np.array([180, 180, 155])

current_key = set()

radius_of_circle = 15

window_size = 160

video = cv2.VideoCapture(0)

while True:
    keyPressed = False
    _, grabbed_Frame = video.read()
    height, width = grabbed_Frame.shape[:2]

    grabbed_Frame = cv2.resize(grabbed_Frame, dsize=(600, height))
    blur_frame = cv2.GaussianBlur(grabbed_Frame, (11, 11), 0)
    hsv_value = cv2.cvtColor(blur_frame, cv2.COLOR_HSV2BGR)

    cover = cv2.inRange(hsv_value, blueLower, blueUpper)

    cover = cv2.erode(cover, None, iterations=2)
    cover = cv2.dilate(cover, None, iterations=2)

    left_cover = cover[:, 0:width//2]
    right_cover = cover[:, width//2:]

    def extract_contour(contours):
        if len(contours) == 2:
            contours = contours[0]
        elif len(contours) == 3:
            contours = contours[1]
        else:
            raise Exception(("Contours tuple must have length 2 or 3,"
                             "otherwise OpenCV changed their cv2.findContours return "
                             "signature. Refer to OpenCV's documentation "
                             "in that case"))

        return contours

    contour_l = cv2.findContours(left_cover.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE
                                 )
    contour_l = extract_contour(contour_l)
    left_centre = None

    contour_r = cv2.findContours(right_cover.copy(),
                                 cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE
                                 )
    contour_r = extract_contour(contour_r)
    right_centre = None

    if len(contour_l) > 0:
        c = max(contour_l, key=cv2.contourArea)
        ((x, y), r) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        left_centre = (int(M["m10"] / (M["m00"] + 0.000001)),
                       int(M["m01"] / (M["m00"]+0.000001)))

    if r > radius_of_circle:
        cv2.circle(grabbed_Frame, (int(x), int(y), ), int(r), (0, 255, 0), 2)
        cv2.circle(grabbed_Frame, left_centre, 5, (0, 255, 0), -1)

        if left_centre[1] < (height/2 - window_size//2):
            cv2.putText(grabbed_Frame, 'LEFT', (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            pyautogui.press('left')
            keyPressed = True
            keyPressed_lr = True
        elif left_centre[1] > (height/2 + window_size//2):
            cv2.putText(grabbed_Frame, 'RIGHT', (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            pyautogui.press('right')
            keyPressed = True
            keyPressed_lr = True

    if len(contour_r):
        c = max(contour_r, key=cv2.contourArea)
        ((x2, y2), r2)
