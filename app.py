import os
from flask import Flask, render_template, request, redirect, send_file
import boto3

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World'

@app.route('/storage')
def storage():
    return  render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
         f = request.files['file']
         f.save(os.path.join('upload-file', f.filename))
         upload_file(f"upload-file/{f.filename}", "experiment-video-upload-bucket")
         return redirect("/storage")


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