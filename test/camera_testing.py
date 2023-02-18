import cv2

# Start video capture
cap = cv2.VideoCapture('20230216_220710.mp4')

# Set the camera's brightness to the maximum value
cap.set(cv2.CAP_PROP_BRIGHTNESS, 1.0)

while True:
    # Read frame from camera
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()
cv2.destroyAllWindows()