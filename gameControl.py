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
