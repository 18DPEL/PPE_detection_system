from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO('last.pt')

# Load video
video_path ='group-of-people-18.jpg'
cap = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = cap.read()

    # Perform object tracking
    results = model.track(frame, persist=True)
    frame_ = results[0].plot()

    # Resize frame for display
    frame_ = cv2.resize(frame_, (800, 600))  # Adjust the size as needed

    # Visualize
    cv2.imshow('frame', frame_)
    if cv2.waitKey(0) & 0xFF == ord('q'):
       break

# Release resources
cap.release()
cv2.destroyAllWindows()
