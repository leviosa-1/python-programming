import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

cap = cv2.VideoCapture(0)  # Checks for the default camera

mpHands = mp.solutions.hands  # Detects hand/finger
hands = mpHands.Hands()  # Complete the initialization configuration of hands
mpDraw = mp.solutions.drawing_utils

# To access the speaker through the pycaw library
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volbar = 400
volper = 0

volMin, volMax, _ = volume.GetVolumeRange()  # Added an underscore to discard unused value

while True:
    success, img = cap.read()  # If the camera works, capture an image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Collection of gesture information
    results = hands.process(imgRGB)  # Complete the image processing.

    lmList = []  # Create an empty list
    if results.multi_hand_landmarks:  # Check if hands are detected
        for handLandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)

    if lmList:
        x1, y1 = lmList[4][1], lmList[4][2]  # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Index finger tip

        cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        length = hypot(x2 - x1, y2 - y1)
        vol = np.interp(length, [30, 350], [volMin, volMax])
        volbar = np.interp(length, [30, 350], [400, 150])
        volper = np.interp(length, [30, 350], [0, 100])

        print(vol, int(length))
        volume.SetMasterVolumeLevelScalar(vol,0,None)  # Corrected the volume control method

        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)
        cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, f"{int(volper)}%", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 98), 3)  # Corrected the font and thickness

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()  # Stop the camera
cv2.destroyAllWindows()  # Close the window
