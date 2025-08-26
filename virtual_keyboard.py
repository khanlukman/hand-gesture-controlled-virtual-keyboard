import cv2
import mediapipe as mp
import numpy as np
import string

print("✅ Virtual keyboard script is running...")

cap = cv2.VideoCapture(0)
print("🔍 Camera opened:", cap.isOpened())

if not cap.isOpened():
    print("❌ Failed to open camera. Exiting.")
    exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

keys = list(string.ascii_uppercase)
key_positions = []
key_width, key_height = 60, 60
cols = 10

for i, key in enumerate(keys):
    x = 100 + (i % cols) * (key_width + 10)
    y = 150 + (i // cols) * (key_height + 10)
    key_positions.append((key, (x, y)))

def draw_keyboard(img, hovered_key=None, pressed_key=None, frame_count=0):
    for idx, (key, (x, y)) in enumerate(key_positions):
        r = int(127 + 127 * np.sin((frame_count + idx) / 5.0))
        g = int(127 + 127 * np.sin((frame_count + idx) / 7.0 + 2))
        b = int(127 + 127 * np.sin((frame_count + idx) / 9.0 + 4))
        color = (b, g, r)

        if key == hovered_key:
            color = (0, 255, 255)
        elif key == pressed_key:
            color = (0, 255, 150)

        cv2.rectangle(img, (x + 4, y + 4), (x + 64, y + 64), (30, 30, 30), -1)
        overlay = img.copy()
        cv2.rectangle(overlay, (x, y), (x + 60, y + 60), color, -1)
        cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)
        cv2.rectangle(img, (x, y), (x + 60, y + 60), color, 2)
        cv2.putText(img, key, (x + 15, y + 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

def detect_keypress(xf, yf):
    for key, (x, y) in key_positions:
        if x < xf < x + key_width and y < yf < y + key_height:
            return key
    return None

typed_text = ''
last_pressed = None
cooldown = 0
frame_count = 0

print("📸 Starting webcam feed...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Could not read frame.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    hovered_key = None
    pressed_key = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = frame.shape
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            x_tip = int(index_tip.x * w)
            y_tip = int(index_tip.y * h)
            x_thumb = int(thumb_tip.x * w)
            y_thumb = int(thumb_tip.y * h)

            cv2.circle(frame, (x_tip, y_tip), 10, (0, 255, 0), -1)
            hovered_key = detect_keypress(x_tip, y_tip)

            distance = np.linalg.norm(np.array([x_tip - x_thumb, y_tip - y_thumb]))

            if distance < 40 and cooldown == 0 and hovered_key:
                if hovered_key != last_pressed:
                    typed_text += hovered_key
                    last_pressed = hovered_key
                    pressed_key = hovered_key
                    cooldown = 10
            elif distance >= 40:
                last_pressed = None

    if cooldown > 0:
        cooldown -= 1

    cv2.rectangle(frame, (40, 30), (900, 90), (10, 10, 10), -1)
    cv2.putText(frame, f"Typed: {typed_text}", (60, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)

    draw_keyboard(frame, hovered_key, pressed_key, frame_count)
    frame_count += 1

    cv2.imshow("🌈 RGB Virtual Keyboard", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("🧹 Cleanup done. Bye! 👋")
