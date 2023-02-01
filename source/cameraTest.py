"""
BEFORE RUNNING: SET ENVIRONMENT
Copy and paste two commands in terminal:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.venv\scripts\activate
"""
import cv2 as cv

# Open the camera
camera = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv.imshow('Camera', frame)
    
    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()

# Close all windows
cv.destroyAllWindows()
