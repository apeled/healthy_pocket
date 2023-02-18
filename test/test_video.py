import cv2

# Open the video file for reading
cap = cv2.VideoCapture('20230216_220710.mp4')
print(cap.isOpened())
# Set the frame number to read
frame_num = 32

# Loop through each frame of the video
for i in range(frame_num):
    ret, frame = cap.read()
    if not ret:
        break

# Check that the frame is not None and has valid dimensions before displaying it
if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
    # Display the 32nd frame in a window
    cv2.imshow('Frame 32', frame)

    # Wait for a key event and exit the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Invalid frame.')
