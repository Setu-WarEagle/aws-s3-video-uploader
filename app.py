import os
from flask import Flask, render_template, request, redirect, send_file, Response
import boto3
import time

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World'

@app.route('/storage')
def storage():
    return  render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    def uploading_progress(req):
        with app.test_request_context():
            request = req
            file = request.files['file']
            yield "Saving the file: {}. Please be patient...."
            file.save(os.path.join('upload-file', file.filename))
            yield "Saved! Starting to upload to S3 ..."
            upload_file(f"upload-file/{file.filename}", "experiment-video-upload-bucket")
            yield "Uploaded to S3! redirecting to home page now..."
            time.sleep(5)
        return

        uploading_progress((request))
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
