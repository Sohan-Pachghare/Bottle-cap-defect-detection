**Bottle Cap Defect Detection**
This project implements a real-time computer vision system to detect defects in bottle caps using a trained YOLO (You Only Look Once) model. It captures video from a webcam, processes the frames to identify faults, and visualizes the results on-screen.

Project Structure
detect_faults.py: The main Python script that runs the real-time inference loop using the webcam.

best.pt: The custom-trained YOLO model weights used for detection.

colab findings/: A directory containing training results and performance metrics:

BoxPR_curve.png: Precision-Recall curve.

confusion_matrix_normalized.png: Normalized confusion matrix showing model accuracy.

results.png: Summary of training results.

**Prerequisites**
To run this project, you need Python installed along with the following libraries:

opencv-python (for video capture and image display)

ultralytics (for loading and running the YOLO model)

Installation
You can install the required dependencies using pip:

Bash

"""pip install opencv-python ultralytics"""
Usage
Place the Model: Ensure the best.pt file is located in the same directory as detect_faults.py.

Run the Script: Execute the Python script to start the webcam feed and detection:

Bash

python detect_faults.py
Operation:

The script will open a window titled "Manufacturing Fault Detection" showing the live feed with bounding boxes around detected defects.

Press the q key to exit the application.

Code Overview
The detect_faults.py script performs the following steps:

Loads the trained YOLO model (best.pt).

Initializes the webcam (source index 0).

Reads frames in a loop, runs the model inference, and annotates the frames with detection results.

Displays the output and handles user input to quit.
