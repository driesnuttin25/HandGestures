# Hand Gesture PDF Navigator
## Description
This project can detect a users hand either swiping to the left or the right. This is achieved using opencv and mediapipe as this provided the most straigth forward path to a request my father made. His proposition was that whilst he was playing piano he did not want to reach forware every time and wanted to simply use his hands to swipe in the air as this would reduce the time away from the keys themselves. With this code, once the user swipes right in the air when a camera is pointed to them, the device will press the right or left key depending on where the user swipes. This project was a little challenge I posed myself and it ended up working much better than I expected.

## Installation
### Prerequisites:

Python 3.6 or newer (Note: Python versions 1.12 are incompatible with MediaPipe. This project was successfully implemented using Python 1.10.)
A functioning webcam
### Dependencies:
Install the necessary Python libraries using pip:
```
pip install opencv-python mediapipe pyautogui
```
### Clone the Repository:
```
https://github.com/driesnuttin25/HandGestures.git
```
### Usage
1) Open your preferred PDF viewer and load a PDF document. Ensure the viewer is set to a mode where keyboard arrows can control page navigation.
2) Execute the script by navigating to the project directory and running:

```
python HandGestures.py
```
3) To navigate, place your hand in the webcam's view: swipe left to move to the next page, and swipe right to return to the previous page.
4) Press the ESC key while the webcam window is active to exit the application.
