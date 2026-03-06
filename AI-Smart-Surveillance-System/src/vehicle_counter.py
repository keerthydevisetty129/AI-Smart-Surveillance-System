from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load traffic video
cap = cv2.VideoCapture("src/videos/traffic.mp4")
while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for r in results:

        boxes = r.boxes.xyxy
        classes = r.boxes.cls
        scores = r.boxes.conf

        for box, cls, conf in zip(boxes, classes, scores):

            x1, y1, x2, y2 = map(int, box)

            label = model.names[int(cls)]
            confidence = float(conf)

            # Detect vehicles only
            if label in ["car", "motorcycle", "bus", "truck"]:

                text = f"{label} {confidence:.2f}"

                cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

                cv2.putText(frame,text,(x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,(255,0,0),2)

    cv2.imshow("Vehicle Detection", frame)

    # press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()