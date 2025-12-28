import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO("best.pt")

# Open webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Run inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the resulting frame
        cv2.imshow("Manufacturing Fault Detection", annotated_frame)

        # Hit 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()