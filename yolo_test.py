from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import numpy as np
import csv
from itertools import zip_longest
from tracker import EuclideanDistTracker
from itertools import zip_longest as izip_longest

app = Flask(__name__)

# YOLO model initialization
model = YOLO("yolov8s.pt")
results_generator = model.predict(source=0, show=True, stream=False)

# Vehicle tracking initialization
tracker = EuclideanDistTracker()

# Color detection parameters
target_color_lower = np.array([0, 0, 0])
target_color_upper = np.array([50, 255, 255])

# Video capture initialization
cap = cv2.VideoCapture(0)  # 0 corresponds to the default webcam, you can change it if you have multiple cameras


# Crossing lines positions
middle_line_position = 225
up_line_position = middle_line_position - 15
down_line_position = middle_line_position + 15

# Initialize counts and lists
up_list = [0, 0, 0, 0]
down_list = [0, 0, 0, 0]
detected_classNames = []

# Detection and suppression thresholds
confThreshold = 0.1
nmsThreshold = 0.2

# Flask route for rendering the webpage
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for video feed
def generate_frames():
    for results in results_generator:
        rendered_frame = results.render()[0]

        # Perform color detection on the frame
        frame_with_color_detection = color_detection(rendered_frame)

        # Vehicle detection and counting
        detection, class_names = vehicle_detection(frame_with_color_detection)

        # Update the tracker
        boxes_ids = tracker.update(detection)

        # Count vehicles based on their positions
        for box_id in boxes_ids:
            count_vehicle(box_id)

        # Encode the frame as JPEG image
        _, jpeg = cv2.imencode('.jpg', frame_with_color_detection)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Flask route for video feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def color_detection(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, target_color_lower, target_color_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center_x = x + w // 2
        center_y = y + h // 2

        if target_color_lower[0] <= hsv_frame[center_y, center_x, 0] <= target_color_upper[0]:
            print("Target color detected!")

    return frame

def vehicle_detection(frame):
    input_size = 320
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (input_size, input_size), [0, 0, 0], 1, crop=False)
    model.setInput(blob)
    layersNames = model.net.getLayerNames()
    outputNames = [(layersNames[i[0] - 1]) for i in model.net.getUnconnectedOutLayers()]
    outputs = model.net.forward(outputNames)

    boxes = []
    classIds = []
    confidence_scores = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]

            if confidence > confThreshold and classId in required_class_index:
                w, h = int(det[2] * width), int(det[3] * height)
                x, y = int((det[0] * width) - w / 2), int((det[1] * height) - h / 2)
                boxes.append([x, y, w, h])
                classIds.append(classId)
                confidence_scores.append(float(confidence))

    return boxes, classIds

def count_vehicle(box_id):
    x, y, w, h, id, index = box_id
    center = find_center(x, y, w, h)
    ix, iy = center

    if (iy > up_line_position) and (iy < middle_line_position):
        if id not in temp_up_list:
            temp_up_list.append(id)
    elif iy < down_line_position and iy > middle_line_position:
        if id not in temp_down_list:
            temp_down_list.append(id)
    elif iy < up_line_position:
        if id in temp_down_list:
            temp_down_list.remove(id)
            up_list[index] = up_list[index] + 1
    elif iy > down_line_position:
        if id in temp_up_list:
            temp_up_list.remove(id)
            down_list[index] = down_list[index] + 1

def find_center(x, y, w, h):
    center_x = x + w // 2
    center_y = y + h // 2
    return center_x, center_y

if __name__ == "__main__":
    app.run(debug=True)
