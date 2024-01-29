import cv2
import os
from flask import Flask, flash, request, redirect, url_for
from image_processing import calculate_humans
from files_operations import download_image, cleanup_memory, allowed_file
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/endpoint1')
def endpoint1():
    number_of_people = calculate_humans("people.png")
    return '<h1>Number of people on the photo: ' + str(number_of_people) + '</h2>'
import cv2

def calculate_humans(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (700, 400))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    humans, _ = hog.detectMultiScale(img, winStride=(4, 4),
                                      padding=(4, 4), scale=1.1)
    return len(humans), humans


image_path = "people.png"
num_humans, humans = calculate_humans(image_path)
print(f'Liczba wykrytych ludzi: {num_humans}')
image = cv2.imread(image_path)
for (x, y, w, h) in humans:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("People detector", image)
    cv2.destroyAllWindows()





@app.route('/endpoint2')
def endpoint2():
    image_link = request.args.get('image-link')
    download_path = download_image(image_link)
    number_of_people = calculate_humans(download_path)
    cleanup_memory(download_path)
    return '<h1>Number of people on the downloaded photo: ' + str(number_of_people) + '</h2>'


@app.route('/endpoint3', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            number_of_people = calculate_humans(filename)
            cleanup_memory(filename)
            return '<h1>Number of people on the uploaded photo: ' + str(number_of_people) + '</h2>'

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
