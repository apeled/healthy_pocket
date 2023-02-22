import os
import cv2
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
# need to add check to make sure file has not already been inputted into dataset


def luma_component_mean(frames):
    """Computes the mean luma value for each frame and stores them in an array. Frames 240 to 6500"""
    signal = []
    for frame_bgr in frames:
        img_ycrcb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2YCrCb)
        mean_of_luma = img_ycrcb[..., 0].mean()
        signal.append(mean_of_luma)

    signal = np.array(signal)[240:6500] * -1
    return signal

def process_video_file(video_file_path):
    cap = cv2.VideoCapture(video_file_path)

    list_of_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        list_of_frames.append(frame)

    cap.release()

    luma_signal = luma_component_mean(list_of_frames) * -1
    return luma_signal

def update_master_dataset(root_dir):
    # Create an empty dataframe to store the results
    results_df = pd.DataFrame()

    # Recursively search through all subdirectories in the root directory
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file is an mp4 file
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                luma_signal = process_video_file(file_path)

                # Limit to 850 frames
                luma_signal = luma_signal[240:6500]

                # Create a new column in the results dataframe with the name of the folder + file name
                folder_name = os.path.basename(root)
                col_name = folder_name + "_" + file
                results_df[col_name] = luma_signal

    # Write the results to a CSV file
    results_df.to_csv("luma_results_full_spec.csv", index_label="Frame")


def plot_from_dataset(csv_file_for_analysis, low_patient_rec, high_patient_rec):
    """Takes in the name of the csv file used for analysis, along with a low and high values for 
    column selection and produces a line plot of the luma values for the specified columns"""
    # Read in the CSV file
    df = pd.read_csv(csv_file_for_analysis)

    # plot frames 240-6500 for patient recodings in columns low_patient_rec to high_patient_rec
    plt.plot(df.iloc[240:6500, 0], df.iloc[240:6500, low_patient_rec:high_patient_rec])
    plt.xlabel('Frame Number')
    plt.ylabel("Luma value")
    plt.title('Plot of recodings ' + str(low_patient_rec) + ' to ' + str(high_patient_rec))
    plt.show()


# Define the root directory for searching
root_dir = "C:\\Users\\amitp\\Documents\\healthy_pocket\\data\\luma_testing\\videos"

plot_from_dataset('luma_results_full_spec.csv', 25, 50)
# update_master_dataset(root_dir)


""" 
# Define the directory to search
root_dir = 'C:\\Users\\amitp\\Documents\\healthy_pocket\\data\\luma_testing\\videos'

# Define the output CSV file
output_file = 'luma_values_dir.csv'

# Create an empty DataFrame to store the luma values
df = pd.DataFrame()

# Loop through each directory and file in the root directory and its subdirectories
for root, dirs, files in os.walk(root_dir):
    for file in files:
        # Check if the file is an MP4 video file
        if file.lower().endswith('.mp4'):
            file_path = os.path.join(root, file)

            # Open the video file for reading
            cap = cv2.VideoCapture(file_path)

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
            luma_signal = luma_component_mean(list_of_frames)

            # Add the luma values to the DataFrame
            df[file] = luma_signal

# Set the index of the DataFrame to be the frame numbers
df.index = range(1, len(df) + 1)

# Save the DataFrame to the output CSV file
df.to_csv(output_file, index_label='Frame')
 """

""" 
def luma_component_mean(frames):
    signal = []
    for frame_bgr in frames:
        img_ycrcb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2YCrCb)
        mean_of_luma = img_ycrcb[..., 0].mean()
        signal.append(mean_of_luma)

    signal = np.array(signal)
    return signal


# Define the folder containing the videos
folder = 'C:\\Users\\amitp\\Documents\\healthy_pocket\\data\\luma_testing\\videos\\00001'

# Create an empty DataFrame to store the luma signals for each video
df = pd.DataFrame()

# Loop through each file in the folder
for filename in os.listdir(folder):
    if filename.endswith('.mp4'):
        # Open the video file for reading
        cap = cv2.VideoCapture(os.path.join(folder, filename))

        # Create a list to store the video frames
        list_of_frames = []

        # Loop through each frame of the video
        frame_count = 0
        while cap.isOpened() and frame_count < 850:
            ret, frame = cap.read()
            if not ret:
                break

            # Append the frame to the list of frames
            list_of_frames.append(frame)
            frame_count += 1

        # Release the video capture
        cap.release()

        # Compute the luma component mean signal
        luma_signal = luma_component_mean(list_of_frames) * -1

        # Add the luma signal to the DataFrame with the filename as the header
        df[filename] = luma_signal

# Add the frame numbers as the index
df.index = range(1, len(df)+1)

# Add a header to the first column
df.columns.name = filename

# Save the DataFrame to a CSV file
df.to_csv('luma_signals.csv')

 """
""" 
import os
import cv2
import numpy as np
import pandas as pd

def luma_component_mean(frames):
    signal = []
    for frame_bgr in frames:
        img_ycrcb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2YCrCb)
        mean_of_luma = img_ycrcb[..., 0].mean()
        signal.append(mean_of_luma)

    signal = np.array(signal)
    return signal

# Define the folder containing the videos
folder = 'C:\\Users\\amitp\\Documents\\healthy_pocket\\data\\luma_testing\\videos\\00001'

# Create an empty DataFrame to store the luma signals for each video
df = pd.DataFrame()

# Loop through each file in the folder
for filename in os.listdir(folder):
    if filename.endswith('.mp4'):
        # Open the video file for reading
        cap = cv2.VideoCapture(os.path.join(folder, filename))

        # Create a list to store the video frames
        list_of_frames = []

        # Loop through each frame of the video
        frame_count = 0
        while cap.isOpened() and frame_count < 850:
            ret, frame = cap.read()
            if not ret:
                break

            # Append the frame to the list of frames
            list_of_frames.append(frame)
            frame_count += 1

        # Release the video capture
        cap.release()

        # Compute the luma component mean signal
        luma_signal = luma_component_mean(list_of_frames) * -1

        # Add the luma signal to the DataFrame with the filename as the header
        df[filename] = luma_signal

# Add the frame numbers as the index
df.index = range(1, len(df)+1)

# Add a header to the first column
df.columns.name = 'File'

# Save the DataFrame to a CSV file
df.to_csv('luma_signals_testing.csv')
 """
