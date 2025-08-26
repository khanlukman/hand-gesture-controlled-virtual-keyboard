# hand-gesture-controlled-virtual-keyboard
 This project is a Hand Gesture Controlled Virtual Keyboard using OpenCV, MediaPipe, and NumPy. It tracks hand landmarks in real time, lets you hover over keys with your index finger, and press them using a pinch gesture with your thumb. Typed text is displayed live with a colorful animated keyboard UI.
🌈 Virtual Keyboard (Hand Gesture Controlled) ✋⌨️

A smart and interactive Virtual Keyboard built with OpenCV, MediaPipe, and NumPy. Instead of pressing physical keys, you can type by hovering your index finger over virtual keys and making a pinch gesture (index + thumb) to press them. The project features real-time hand tracking, animated RGB keyboard UI, and live text feedback.

🚀 Features

Hand Tracking: Detects hand landmarks in real time using MediaPipe.

Gesture-Based Typing: Hover over a key with your index finger and pinch with your thumb to select.

Dynamic RGB Keyboard: Keys glow with animated colors for a modern look.

Real-Time Feedback: Displays typed text live on screen.

Cooldown Mechanism: Prevents duplicate accidental key presses.

Webcam Support: Runs smoothly with any standard camera.

🛠 Process & Implementation

OpenCV: Captures and displays webcam frames.

MediaPipe Hands: Detects 21 hand landmarks for gesture control.

NumPy: Calculates distance between index and thumb for press detection.

Keyboard Layout: A-Z arranged in a grid with interactive hover/press effects.

UI Rendering: Animated key colors with hover and press highlights.

✅ Validations

Hovered Key: Highlighted in yellow.

Pressed Key: Highlighted in green.

Cooldown: Avoids multiple unwanted presses.

💻 Setup

Clone the repository:

git clone <your-repo-link>
cd virtual-keyboard


Install dependencies:

pip install opencv-python mediapipe numpy


Run the script:

python virtual_keyboard.py

🎯 Key Takeaways

Gesture Control Development: Real-time interaction with computer vision.

UI & Effects: Built animated RGB keyboard for better UX.

Game Logic: Hover detection, press recognition, and cooldown handling
