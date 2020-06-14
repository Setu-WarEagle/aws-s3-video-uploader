import os
from flask import Flask, render_template, request, redirect, send_file, make_response, jsonify
import boto3
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def entry_point():
    return 'Hello World'

@app.route('/')
def storage():
    return render_template('upload-video.html')

@app.route("/upload-video", methods=["GET", "POST"])
def upload_video():
    """
    Post : uploads the file.
    GET  : renders the page.
    reference:
    https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/upload
    https://pythonise.com/articles/upload-progress-bar-xmlhttprequest
    :return: 200 response if success.
    """
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join('upload-file', file.filename))
        print("File uploaded to server!")

        #s3 upload.
        upload_file(f"upload-file/{file.filename}", "experiment-video-upload-bucket")
        res = make_response(jsonify({"message": "File uploaded"}), 200)

        #remove the file from local server.
        os.remove(f"upload-file/{file.filename}")

        return res

    return render_template("upload-video.html")

def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')