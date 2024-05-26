# Hand Gesture Control for Mouse using OpenCV and MediaPipe

This project demonstrates how to use hand gestures to control mouse actions using OpenCV, MediaPipe, and PyAutoGUI. By tracking hand landmarks, it enables functionalities like moving the cursor, left-clicking, and right-clicking based on specific finger positions.

## Features

- **Cursor Movement**: Move the cursor based on the position of the middle finger.
- **Left Click**: Perform a left-click when the thumb and index finger tips are close together.
- **Right Click**: Perform a right-click when the thumb and middle finger tips are close together.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. **Clone the Repository**:
   ```bash
   git clone  https://github.com/Deepan-CodeBuster/-Hand-Gesture-Control-for-Mouse-using-OpenCV-and-MediaPipe.git
   cd hand-gesture-control
   ```

2. **Install Dependencies**:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Usage

1. **Run the Script**:
   ```bash
   python hand_gesture_control.py
   ```

2. **Interact with the Script**:
   - Move your hand in front of the webcam.
   - Use your middle finger to move the cursor.
   - Touch the thumb and index finger tips together to perform a left-click.
   - Touch the thumb and middle finger tips together to perform a right-click.



## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.
