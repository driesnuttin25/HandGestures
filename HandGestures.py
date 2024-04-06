import cv2
import mediapipe as mp
import time
import pyautogui

# Setup MediaPipe for hand detection and tracking.
# This includes initializing the hand tracking module with specific parameters
# for detection confidence and tracking confidence.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Initialize variables for gesture detection.
# 'gesture_state' tracks the current state of hand gesture.
# 'start_x_position' holds the initial X position of the hand for gesture detection.
# 'gesture_threshold' defines the minimum movement required to detect a gesture.
# 'gesture_delay' sets a cooldown period to prevent rapid gesture detection.
# 'last_gesture_time' records the time when the last gesture was detected.
# 'page_count' keeps track of the number of pages navigated.
gesture_state = "neutral"
start_x_position = None
gesture_threshold = 0.09
gesture_delay = 2
last_gesture_time = 0
page_count = 0

# Start capturing video from the webcam.
cap = cv2.VideoCapture(0)

# Main loop for hand tracking and gesture detection.
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB and process it with MediaPipe to detect hands.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    hand_detected = False
    current_time = time.time()

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame for visualization.
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate the hand's movement to detect gestures.
            wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
            hand_detected = True

            if gesture_state == "neutral" and start_x_position is None:
                start_x_position = wrist_x

            if start_x_position is not None and current_time - last_gesture_time > gesture_delay:
                dx = wrist_x - start_x_position

                # Detect swipe gestures based on hand movement and update page count.
                if abs(dx) > gesture_threshold:
                    if dx < 0:  # Adjust for camera mirroring.
                        gesture_state = "moved_right"
                        page_count += 1
                        print(f"Moved Right - Page Count: {page_count}")
                        pyautogui.press('right')
                    else:
                        gesture_state = "moved_left"
                        page_count -= 1
                        print(f"Moved Left - Page Count: {page_count}")
                        pyautogui.press('left')
                    
                    # Reset gesture detection.
                    start_x_position = None
                    gesture_state = "neutral"
                    last_gesture_time = current_time

    # Reset state if no hand is detected in the frame.
    if not hand_detected:
        start_x_position = None
        gesture_state = "neutral"

    # Display the frame with hand tracking visualization.
    cv2.imshow('Hand Tracking', frame)

    # Exit the loop if the Escape key is pressed.
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the webcam and destroy all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
