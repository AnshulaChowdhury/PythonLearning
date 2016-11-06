from flask import Flask
app = Flask_APP

@app.route('/')
def hello_world():
    return 'Hello, World!'
    print('Hello, world!')