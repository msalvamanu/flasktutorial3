from flask import Flask 
app = Flask (__name__)

@app.route ("/")

def hello_world ():
    return "<p> Hello, Manuel, you will learn Falsk now </p>"


