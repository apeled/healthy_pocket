import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Luma code copied from the github found online
def luma_component_mean(frames):
    signal = []
    for frame_bgr in frames:
        img_ycrcb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2YCrCb)
        mean_of_luma = img_ycrcb[..., 0].mean()
        signal.append(mean_of_luma)

    signal = np.array(signal)
    # samples_to_skip = kwargs["initial_skip_seconds"] * self.sample_rate
    # ignore first second because of auto exposure
    # signal = signal[samples_to_skip:]
    return signal


# Open the video file for reading
cap = cv2.VideoCapture('C:\\Users\\amitp\\Documents\healthy_pocket\\test\\20230216_220710.mp4')

# Create a list to store the video frames
list_of_frames = []

# Loop through each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    # Append the frame to the list of frames
    list_of_frames.append(frame)

# Release the video capture
cap.release()

# Compute the luma component mean signal
luma_signal = luma_component_mean(list_of_frames) * -1

print(luma_signal)
"""
plt.plot(luma_signal)
plt.show()
# Set the title and axis labels
plt.set_title("Extracted PPG Signals with Luma Component Mean")
plt.set_xlabel('Frame')
plt.set_ylabel('Signal Value')

# Add a legend and save the figure
plt.legend()
"""
