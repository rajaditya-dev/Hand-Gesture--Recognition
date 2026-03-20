import cv2
import mediapipe as mp
import joblib
import pandas as pd

model = joblib.load("sign_model.pkl")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not detected")
    exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=4)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success or img is None:
        continue

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            cols = []
            for i in range(21):
                cols += [f"x{i}", f"y{i}", f"z{i}"]

            df = pd.DataFrame([landmarks], columns=cols)

            prediction = model.predict(df)
            probs = model.predict_proba(df)

            label = prediction[0]
            confidence = max(probs[0]) * 100

            wrist = hand.landmark[0]
            x = int(wrist.x * w)
            y = int(wrist.y * h)

            cv2.putText(img,
                        f"{label} ({confidence:.1f}%)",
                        (x - 60, y - 25),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 0),
                        2)

            bar_length = int(confidence * 2)  # scale
            cv2.rectangle(img,
                          (x - 60, y),
                          (x - 60 + bar_length, y + 8),
                          (0, 0, 0),
                          -1)

            cv2.rectangle(img,
                          (x - 60, y),
                          (x + 140, y + 8),
                          (255, 255, 255),
                          1)

    cv2.imshow("AI Multi-Hand Sign Detector", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()