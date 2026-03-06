from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for r in results:

        boxes = r.boxes.xyxy
        classes = r.boxes.cls

        for box, cls in zip(boxes, classes):

            x1, y1, x2, y2 = map(int, box)
            class_id = int(cls)

            if class_id == 67:

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

                cv2.putText(frame,"Mobile Phone",
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,(0,0,255),2)

    cv2.imshow("Phone Detection",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()