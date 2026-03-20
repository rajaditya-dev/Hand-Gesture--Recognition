import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

finger_tips = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            lm_list = []

            for lm in hand.landmark:
                lm_list.append(lm)

            # Thumb (x-axis check)
            if lm_list[4].x > lm_list[3].x:
                finger_count += 1

            # Other 4 fingers (y-axis check)
            for tip in finger_tips[1:]:
                if lm_list[tip].y < lm_list[tip - 2].y:
                    finger_count += 1

            mp_draw.draw_landmarks(
                img, hand, mp_hands.HAND_CONNECTIONS
            )

    cv2.putText(
        img,
        f"Fingers: {finger_count}",
        (30, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Finger Count", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
