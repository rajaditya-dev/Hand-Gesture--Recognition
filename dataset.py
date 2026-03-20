import cv2
import mediapipe as mp
import csv
import os

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=4)
mp_draw = mp.solutions.drawing_utils

file_name = "sign_dataset.csv"

if not os.path.exists(file_name):
    with open(file_name, mode="w", newline="") as f:
        writer = csv.writer(f)
        header = []
        for i in range(21):
            header += [f"x{i}", f"y{i}", f"z{i}"]
        header.append("label")
        writer.writerow(header)

# print("Press:")
# print("H for HELLO")
# print("S for STOP")
# print("P for PEACE")
# print("O for OK")
# print("T for APPROVED")
# print("I for LUV U")
# print("M for MIDDLE FINGER")
# print("N for NO")

print("Q to quit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
            landmarks = []
            for lm in hand.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

    cv2.imshow("Dataset Collector", img)
    key = cv2.waitKey(1)

    if key == ord("h") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["HELLO"])
        print("Saved HELLO")

    elif key == ord("s") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["STOP"])
        print("Saved STOP")

    elif key == ord("p") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["PEACE"])
        print("Saved PEACE")

    elif key == ord("o") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["OK"])
        print("Saved OK")


    elif key == ord("t") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["APPROVED"])
        print("Saved APPROVED")
    

    elif key == ord("i") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["I LOvE YOU"])
        print("Saved I LOVE YOU")


    elif key == ord("m") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["*****"])
        print("Saved ******")



    elif key == ord("n") and results.multi_hand_landmarks:
        with open(file_name, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(landmarks + ["NO"])
        print("Saved NO")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
