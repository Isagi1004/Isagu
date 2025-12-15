import cv2
import numpy as np
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize webcam
cap = cv2.VideoCapture(0)

# Hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
# Not using mp_draw anymore

# Volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol, max_vol = vol_range[0], vol_range[1]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            if lm_list:
                x1, y1 = lm_list[4]   # Thumb tip
                x2, y2 = lm_list[8]   # Index finger tip
                length = np.hypot(x2 - x1, y2 - y1)

                # Volume calculation
                vol = np.interp(length, [30, 200], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

                # Visuals
                vol_bar = np.interp(length, [30, 200], [400, 150])
                vol_perc = np.interp(length, [30, 200], [0, 100])

                # Blue neon circles
                color = (255, 100, 255) if vol_perc < 100 else (255, 255, 0)
                glow = (255, 255, 255) if vol_perc == 100 else color
                cv2.circle(img, (x1, y1), 12, glow, cv2.FILLED)
                cv2.circle(img, (x2, y2), 12, glow, cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), glow, 3)

                # Glowing bar + shadow box
                overlay = img.copy()
                cv2.rectangle(overlay, (50, 150), (85, 400), (100, 100, 255), -1)
                cv2.rectangle(overlay, (50, int(vol_bar)), (85, 400), (0, 255, 255), -1)
                alpha = 0.3
                img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

                # Volume %
                font_color = (255, 255, 255)
                if vol_perc == 100:
                    cv2.putText(img, "MAX POWER!!", (30, 100), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 255), 3)
                    for i in range(10):  # Fake "sparks"
                        x = np.random.randint(0, img.shape[1])
                        y = np.random.randint(0, img.shape[0])
                        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)

                cv2.putText(img, f'{int(vol_perc)}%', (40, 440), cv2.FONT_HERSHEY_SIMPLEX, 1, font_color, 2)

    # Dark overlay system feel
    cv2.rectangle(img, (0, 0), (img.shape[1], 50), (0, 0, 0), -1)
    cv2.putText(img, "Nah I'd Blast", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Shadow Volume Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
