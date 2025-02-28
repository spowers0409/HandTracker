import cv2
import mediapipe as mp

# MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Hand tracking model
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)

# Finger tip landmark indices
finger_tips = [4, 8, 12, 16, 20]

# Start webcam capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip camerae frame horizaontally
    frame = cv2.flip(frame, 1)

    # RGB Frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hands
    results = hands.process(rgb_frame)

    total_finger_count = 0

    if results.multi_hand_landmarks:
        for hand_idx, (hand_landmarks, hand_label) in enumerate(zip(results.multi_hand_landmarks, results.multi_handedness)):
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Left hand right hand label
            # Not working
            hand_type = hand_label.classification[0].label

            # Count fingers
            if lm_list:
                fingers = []

                # Thumb logic to properly count the opposite facing thumbs
                thumb_tip_x = lm_list[finger_tips[0]][0]
                thumb_base_x = lm_list[finger_tips[0] - 1][0]

                if hand_type == "Right":
                    fingers.append(1 if thumb_tip_x < thumb_base_x else 0)
                else:
                    fingers.append(1 if thumb_tip_x > thumb_base_x else 0)

                # Finger logic
                for tip in finger_tips[1:]:
                    fingers.append(1 if lm_list[tip][1] < lm_list[tip - 2][1] else 0)

                hand_finger_count = sum(fingers)
                total_finger_count += hand_finger_count

            # Hand frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Count fingers
    cv2.putText(frame, f"Total Fingers: {total_finger_count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Finger Counter", frame)

    # Exit on q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
