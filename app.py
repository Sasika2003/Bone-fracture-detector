from flask import Flask, render_template, request
from keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = load_model('my_keras_model.h5')

# Function to classify bone fractures
def classify_bone_fracture(model, image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)

    if prediction <= 0.5:
        return "Bone Fracture"
    else:
        return "No Bone Fracture"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', message='No file selected')

        if file:
            image_path = "static/images/uploaded_image.jpg"
            file.save(image_path)

            result = classify_bone_fracture(model, image_path)

            return render_template('result.html', result=result, image_path=image_path)

if __name__ == '__main__':
    app.run()
