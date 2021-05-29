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
