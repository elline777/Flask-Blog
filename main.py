from flask import Flask, request, jsonify, abort
from datetime import datetime

from model.post import Post
from model.user import User

app = Flask(__name__)

API_ROOT = "/api/v1"
POST_API_ROOT = API_ROOT + "/post"

storage = {
    'id_counter': 0,
    'posts': {}
}

users = {
    1: User(1, 'admin'),
    2: User(2, 'editor')
}

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        'error_code': 404,
        'error_text': 'Page not found'
    })

@app.errorhandler(400)
def page_not_found(error):
    return jsonify({
        'error_code': 400,
        'error_text': 'Bad request'
    })

@app.route(POST_API_ROOT + '/', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json:
        abort(400)

    storage['id_counter'] += 1
    post_id = storage['id_counter']
    title = request.json['title']
    text = request.json.get('text', '')
    author_id = request.json.get('author_id', 1)
    author = users.get(author_id, users[1])
    published = datetime.now()
    post = Post(post_id, title, text, published, author)
    storage['posts'][post_id] = post
    return jsonify(post.serialize())


@app.route(POST_API_ROOT + '/', methods=['GET'])
def list_posts():
    return jsonify({'posts': [post.serialize() for post in storage['posts'].values()]})


@app.route(POST_API_ROOT + '/<int:_id>/', methods=['GET'])
def read_post(_id: int):
    if _id not in storage['posts']:
        abort(404)
    post = storage['posts'][_id]
    return jsonify(post.serialize())


@app.route(POST_API_ROOT + '/<int:_id>/', methods=['PUT'])
def update_post(_id: int):
    if _id not in storage['posts']:
        abort(404)
    if not request.json:
        abort(400)

    storage['posts'][_id].title = request.json.get('title', storage['posts'][_id].title)
    storage['posts'][_id].text = request.json.get('text', storage['posts'][_id].text)

    return jsonify(storage['posts'][_id].serialize())


@app.route(POST_API_ROOT + '/<int:_id>/', methods=['DELETE'])
def delete_post(_id: int):
    if _id not in storage['posts']:
        abort(404)
    del storage['posts'][_id]
    return jsonify({'result': True})


