import cv2
import numpy as np
import csv

# Open the video file for reading
cap = cv2.VideoCapture('video.mp4')

# Create a CSV file to store the luma values
with open('luma_values.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Frame', 'Luma'])

    # Loop through each frame of the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate the luma component of the grayscale frame
        luma = np.mean(gray)

        # Write the frame number and luma value to the CSV file
        writer.writerow([cap.get(cv2.CAP_PROP_POS_FRAMES), luma])

    # Release the video capture and close the CSV file
    cap.release()
