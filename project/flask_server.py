import json
from flask import Flask, request, send_file, render_template, jsonify
from flasgger import Swagger
import cv2
from project.handlers.Constants import const
import os
from image_transform_agent import ImageTransformAgent

app = Flask(__name__)
swagger = Swagger(app)
output_filename = None


@app.route('/transformimage/',methods=['POST'])
def trnasformImage():
    """
        This examples uses flasgger.
        It works also with swag_from, schemas and spec_dict
        ---
        summary: Transform image with providing operations in sequence as image
            processing operations and get the output image as response
        consumes:
         - multipart/form-data
        produces:
         - image/png
         - image/tiff
         - image/jpeg
         - image/bmp
         - image/pic
        parameters:
         - in: formData
           name: document
           description: The image file to upload
           required: true
           type: file
         - in: formData
           name: datas
           description: image processing operation list
           type: string
           required: true
        responses:
         '200':
           description: output image will be returned as response
           schema:
            type: file
    """
    print(request)
    print(request.form)
    print(request.files)
    posted_file = request.files['document']
    posted_data = json.loads(request.form['datas'])
    # Save original image to temporary location.
    temp_image_filepath = os.path.join(const.TEMP_IMAGE_FOLDER, posted_file.filename)

    print(temp_image_filepath)
    posted_file.save(temp_image_filepath)

    img = cv2.imread(temp_image_filepath)
    image_transform_agent = ImageTransformAgent()
    print(type(img))
    list_of_operations = list()
    list_of_operations.append({"name": const.ORIGINAL, "img": img})
    list_of_operations.extend(posted_data)
    print(list_of_operations)
    requests = list_of_operations

    """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
    output_img = image_transform_agent.agent(requests)
    output_image_filepath = os.path.join(const.TEMP_IMAGE_FOLDER, f"Converted_{posted_file.filename}")
    cv2.imwrite(output_image_filepath, output_img)
    return send_file(output_image_filepath, as_attachment=True)

    return


@app.route('/test', methods=['POST'])
def create_task():
    return jsonify({'task': 'task'}), 201

@app.route('/')
def upload_form():
    return render_template('download.html')


@app.route('/download')
def download_file():
    return send_file(output_filename, as_attachment=True, mimetype="image/jpeg")


app.run(debug=True)