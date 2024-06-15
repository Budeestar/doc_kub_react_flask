from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import cv2
import base64
import numpy as np
import json
from yolo import run_yolo

app = Flask(__name__)
CORS(app, origins=[front-end-deployment-url])

@app.route('/download', methods=['GET'])
def download_file():
    file_name = request.args.get('file')
    return send_file(file_name, as_attachment=True)

@app.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error no file': 'No selected file'})

    try:
        image_data = file.read()
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        result = run_yolo(image)
        _, buffer = cv2.imencode('.jpg', result['processed_image'])
        base64_image = base64.b64encode(buffer).decode('utf-8')
        cv2.imwrite("yolo_processed.jpg", cv2.imdecode(np.frombuffer(base64.b64decode(base64_image), np.uint8), cv2.IMREAD_COLOR))
        result['processed_image'] = base64_image
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
