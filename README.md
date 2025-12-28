# Bottle Cap Defect Detection

This project implements a real-time computer vision system to detect defects in bottle caps using a trained YOLO (You Only Look Once) model. It captures video from a webcam, processes the frames to identify faults, and visualizes the results on-screen.

## Project Structure

* **detect_faults.py**: The main Python script that runs the real-time inference loop using the webcam.
* **best.pt**: The custom-trained YOLO model weights used for detection.
* **colab findings/**: A directory containing training results and performance metrics:
    * **BoxPR_curve.png**: Precision-Recall curve.
    * **confusion_matrix_normalized.png**: Normalized confusion matrix showing model accuracy.
    * **results.png**: Summary of training results.

## Prerequisites

To run this project, you need Python installed along with the following libraries:
* **opencv-python**: for video capture and image display.
* **ultralytics**: for loading and running the YOLO model.

## Installation

You can install the required dependencies using pip:

```bash
pip install opencv-python ultralytics
```
