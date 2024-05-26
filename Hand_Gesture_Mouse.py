import cv2
import mediapipe as mp
import pyautogui
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Start video capture
cam = cv2.VideoCapture(0)

# Get screen size
screen_w, screen_h = pyautogui.size()

# Initialize clicking flag
clicking = False

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    # Check if hand(s) are detected
    if results.multi_hand_landmarks:
        # Get landmarks of the first hand
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get thumb, index finger, and middle finger tip coordinates
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

        # Calculate Euclidean distance between thumb and index finger tips
        thumb_index_distance = math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)

        # Draw circles at thumb, index finger, and middle finger tips
        thumb_x = int(thumb_tip.x * frame.shape[1])
        thumb_y = int(thumb_tip.y * frame.shape[0])
        index_x = int(index_tip.x * frame.shape[1])
        index_y = int(index_tip.y * frame.shape[0])
        middle_x = int(middle_tip.x * frame.shape[1])
        middle_y = int(middle_tip.y * frame.shape[0])
        cv2.circle(frame, (thumb_x, thumb_y), 5, (0, 255, 0), -1)
        cv2.circle(frame, (index_x, index_y), 5, (0, 0, 255), -1)
        cv2.circle(frame, (middle_x, middle_y), 5, (255, 0, 0), -1)

        # Move cursor to middle finger position
        screen_x = int(screen_w * (middle_x / frame.shape[1]))
        screen_y = int(screen_h * (middle_y / frame.shape[0]))
        pyautogui.moveTo(screen_x, screen_y)

        # Check if thumb and index finger are close enough to perform a click
        if thumb_index_distance < 0.05:  # Adjust threshold as needed
            if not clicking:
                pyautogui.mouseDown()
                clicking = True
        else:
            if clicking:
                pyautogui.mouseUp()
                clicking = False

        # Check if thumb and middle finger are close enough to perform a right-click
        thumb_middle_distance = math.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2)
        if thumb_middle_distance < 0.05:  # Adjust threshold as needed
            pyautogui.rightClick()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cam.release()
    cv2.destroyAllWindows()
    # Display the frame
    cv2.imshow("Thumb-Index Finger Clicking", frame)

