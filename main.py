from flask import Flask
from model.post import Post

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"