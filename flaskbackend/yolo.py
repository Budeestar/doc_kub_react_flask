import cv2
from ultralytics import YOLO
import cvzone
import numpy as np
import pandas as pd
from collections import Counter

def run_yolo(image):
    # Load YOLO model
    model = YOLO("yolov8m.pt")

    # Load COCO class list
    with open("coco.txt", "r") as my_file:
        data = my_file.read()
    class_list = data.split("\n")

    # Object detection on the input image
    results = model.predict(image)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    object_classes = []

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        obj_class = class_list[d]
        object_classes.append(obj_class)
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cvzone.putTextRect(image, f'{obj_class}', (x2, y2), 1, 1)

    # Count objects in the image
    counter = Counter(object_classes)
    object_count = {}
    for obj, count in counter.items():
        object_count[obj] = count

    return {'processed_image': image, 'object_count': object_count}
