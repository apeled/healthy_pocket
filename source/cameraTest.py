import cv2

# Open the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()

# Close all windows
cv2.destroyAllWindows()
