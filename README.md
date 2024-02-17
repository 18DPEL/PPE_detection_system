# PPE_detection_system

This repository contains a Python script for object tracking using YOLO (You Only Look Once) deep learning model. The script utilizes the ultralytics library to load the YOLO model and ppe detection on a video file.

# in this project i am using custom data which is annotated by me each and every image then i build the custom model by using yolov8n pre-trained weights 

# Installation
Clone the repository to your local machine.
Install the required libraries by running pip install -r requirements.txt.
Usage
Download the YOLO weights file (last(2).pt and best(2).pt) and place it in the root directory of the project.
Update the video_path variable in the script with the path to the video file you want to PPE detection on.
Run the script to start the object tracking process.
Press the 'q' key to exit the tracking process.
# Customization
Model: You can use different YOLO models by replacing the last(2).pt and best(2)  file with other YOLO weights files.
Frame Size: Adjust the frame size in the cv2.resize function to change the size of the displayed frames.
# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.



