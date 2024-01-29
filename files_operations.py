import os
import requests

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def download_image(image_url):
    download_path = 'downloaded_image.jpg'
    img_data = requests.get(image_url).content
    with open(download_path, 'wb') as handler:
        handler.write(img_data)

    return download_path


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def cleanup_memory(download_path):
    os.remove(download_path)
