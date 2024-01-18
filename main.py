from flask import Flask, request, jsonify, abort
from datetime import datetime

from model.post import Post
from model.post import User

app = Flask(__name__)

API_ROOT = "/api/v1"
POST_API_ROOT = API_ROOT + "/post"

posts = []
users = {
    1: User(1, 'admin'),
    2: User(2, 'editor')
}

@app.route(POST_API_ROOT + '/', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        abort(400)

    if len(posts) == 0:
        post_id = 1
    else:
        post_id = posts[-1]._id + 1
    title = request.json['title']
    text = request.json.get('text', '')
    author_id = request.json.get('author_id', 1)
    author = users[author_id]
    published = datetime.now()
    post = Post(post_id, title, text, published, author)
    posts.append(post)
    return jsonify({'posts': [post.serialize() for post in posts]})

@app.route(POST_API_ROOT + '/', methods=['GET'])
def list_posts():
    return jsonify({'posts': [post.serialize() for post in posts]})

@app.route(POST_API_ROOT + '/<int:_id>/', methods=['GET'])
def read_post(_id: int):
    pass

@app.route(POST_API_ROOT + '/<int:_id>/', methods=['PUT'])
def update_post(_id: int):
    pass

@app.route(POST_API_ROOT + '/<int:_id>/', methods=['DELETE'])
def delete_post():
    pass

