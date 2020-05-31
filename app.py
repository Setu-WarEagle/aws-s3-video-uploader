import os
from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World'

@app.route('/storage')
def storage():
    return  render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)