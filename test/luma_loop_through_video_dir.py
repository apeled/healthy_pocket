"""
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
"""
import time
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from signal_processing import SignalPreprocessor as sig
import concurrent.futures

# import concurrent.futures
# import csv
# from moviepy.editor import VideoFileClip
# import subprocess

# need to add check to make sure file has not already been inputted into dataset


def luma_component_mean(frame, luma_signal):
    """Computes the mean luma value for each frame and returns the value. Multiplication by -1 applied"""
    img_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    mean_of_luma = img_ycrcb[..., 0].mean() * -1
    luma_signal.append(mean_of_luma)
    return luma_signal

def process_video_file(video_file_path):
    """Processes a video frame-by-frame. References luma_component_mena function to calculate the luma value for each respective frame.
    Takes in a video_file_path (string) and returns a final_signal (array)"""
    # Using cv2, open the video with respective path
    cap = cv2.VideoCapture(video_file_path)

    # Get FPS of video
    FPS = cap.get(cv2.CAP_PROP_FPS)

    # Create an empty list to wich the luma values will be appended to later
    luma_signal = []
    
    # While the video is open, analyze it frame by frame, prefrom luma calculation, and append the frames value to luma_signal list
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            executor.submit(luma_component_mean, frame, luma_signal)
            
        
    cap.release() # release the video

    # Final signal is an array that has luma values for frames between 3 and 33 seconds of recording. 
    start_recording_values = FPS*3
    stop_recording_values = FPS*33
    
    final_signal = np.array(luma_signal)[int(start_recording_values):int(stop_recording_values)]
    
    ### TODO: If filter is disired, uncomment whichever is needed ###

    # final_signal = sig.rolling_average(signal=luma_signal)
    # final_signal = sig.butter_lowpass_filter(signal=luma_signal, low=2, filter_order=2)
    # final_signal = sig.butter_highpass_filter(signal=luma_signal, cutoff=0.5, order=2)
    
    print("The FPS of this video was: " + str(int(FPS)))
    print("Please adjust the file name and its coresponding column name in the csv, if needed.")
    return final_signal

def update_master_dataset(root_dir, csv_filename):
    # Create an empty dataframe to store the results
    results_df = pd.DataFrame()

    # Recursively search through all subdirectories in the root directory
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Check if the file is an mp4 file
            if file.endswith(".MOV") or file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                print("Working on video" + file)
                start_time_for_video = time.time()
                luma_signal = process_video_file(file_path)

                # Create a new column in the results dataframe with the name of the folder + file name
                # folder_name = os.path.basename(root)
                col_name = file
                results_df[col_name] = pd.Series(luma_signal)
                print("Finished with video: " + file + "      --- %s seconds ---" % (time.time() - start_time_for_video))

    # Write the results to a CSV file
    results_df.to_csv(csv_filename, index_label="Frame")

def plot_from_dataset(csv_file_for_analysis):#, low_patient_rec=0, high_patient_rec=0):
    """Takes in the name of the csv file used for analysis, along with a low and high values for 
    column selection and produces a line plot of the luma values for the specified columns"""
    """Might need to pip install pyqt5"""
    
    # Read in the CSV file
    df = pd.read_csv(csv_file_for_analysis)

    # plot frames 240-6500 for patient recodings in columns low_patient_rec to high_patient_rec
    plt.plot(df.iloc[:, 0], df.iloc[:, 1])# low_patient_rec:high_patient_rec+1])
    plt.xlabel('Frame Number')
    plt.ylabel("Luma value")
    # plt.title('Plot of recodings ' + str(low_patient_rec) + ' to ' + str(high_patient_rec))
    plt.show()


start_time = time.time()
# RUN TO LOOP THROUGH VIDEOS IN root_dir

# Define the root directory for searching
root_dir = "C:\\Users\\amitp\\Documents\\healthy_pocket\\data\\luma_testing\\drive-download-20230303T003957Z-001\\Amit\\New Folder"
csv_filename = "speed_test.csv"
update_master_dataset(root_dir, csv_filename)

# plot_from_dataset('speed_test.csv')

print("TOTAL RUNTIME --- %s seconds ---" % (time.time() - start_time))

