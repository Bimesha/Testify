from flask import Flask, request, render_template, redirect, url_for
import os
from PIL import Image
import pytesseract
import string

app = Flask(__name__)

# Ensure the 'uploads' directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    # Remove unwanted characters
    text = text.replace('"', '').replace("'", "")
    return text


def process_text(text):
    # Remove punctuation
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        extracted_text = extract_text(file_path)
        processed_text = process_text(extracted_text)
        return render_template('result.html', text=processed_text)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

