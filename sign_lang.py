import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

finger_tips = [4, 8, 12, 16, 20]

def get_finger_states(lm, hand_label):
    fingers = []

    if hand_label == "Right":
        fingers.append(lm[4].x > lm[3].x)
    else:  
        fingers.append(lm[4].x < lm[3].x)

    finger_tips = [8, 12, 16, 20]
    for tip in finger_tips:
        fingers.append(lm[tip].y < lm[tip - 2].y)

    return fingers



while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for idx, hand in enumerate(results.multi_hand_landmarks):

            lm = hand.landmark
            hand_label = results.multi_handedness[idx].classification[0].label
            fingers = get_finger_states(lm, hand_label)


            sign_text = "Unknown"

            # ✋ HELLO
            if fingers == [1, 1, 1, 1, 1]:
                sign_text = "HELLO"

            # ✊ STOP
            elif fingers == [0, 0, 0, 0, 0]:
                sign_text = "STOP"

            # ✌️ PEACE
            elif fingers == [0, 1, 1, 0, 0] or fingers == [1, 1, 1, 0, 0]:
                sign_text = "PEACE"

            hand_label = results.multi_handedness[idx].classification[0].label

            wrist_x = int(lm[0].x * w)
            wrist_y = int(lm[0].y * h)

            mp_draw.draw_landmarks(
                img, hand, mp_hands.HAND_CONNECTIONS
            )

            cv2.putText(
                img,
                f"{hand_label}: {sign_text}",
                (wrist_x - 40, wrist_y - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

    cv2.imshow("Multi-Hand Sign Language Detector", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
