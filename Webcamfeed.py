import cv2
import numpy as np
from IPython.display import display
from ipywidgets import widgets
from ipywebrtc import CameraStream, ImageRecorder
from google.colab.patches import cv2_imshow
import time

# Create a CameraStream object with the correct constraints
camera = CameraStream(constraints={'video': True})

# Display the camera widget
display(camera)

# Function to capture a frame from the camera stream
def capture_frame(change):
    global frame
    image_array = np.frombuffer(recorder.image.value, dtype=np.uint8)
    frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Create an ImageRecorder to capture frames from the camera stream
recorder = ImageRecorder(stream=camera)
recorder.image.observe(capture_frame, names='value')

# Display the recorder widget
display(recorder)

# Variable to store the frame
frame = None

# Main loop to process video frames
start_time = time.time()
while time.time() - start_time < 10:  # Run the loop for 10 seconds
    if frame is not None:
        # Display the frame using OpenCV
        cv2_imshow(frame)

        # Processing example: Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2_imshow(gray)

        # Reset frame to None
        frame = None

    # Small sleep to avoid busy-waiting
    time.sleep(0.1)

cv2.destroyAllWindows()