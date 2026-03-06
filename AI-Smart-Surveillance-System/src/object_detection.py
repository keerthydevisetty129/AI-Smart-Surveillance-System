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
        scores = r.boxes.conf

        for box, cls, conf in zip(boxes, classes, scores):

            x1, y1, x2, y2 = map(int, box)

            label = model.names[int(cls)]
            confidence = float(conf)

            text = f"{label} {confidence:.2f}"

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.putText(frame,text,(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,(0,255,0),2)

            # Alert if mobile detected
            if label == "cell phone":

                cv2.putText(frame,"PHONE DETECTED!",
                            (50,100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0,0,255),
                            3)

                print("⚠️ Phone detected!")

    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()