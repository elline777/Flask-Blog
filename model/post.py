from model.user import User


class Post:
    def __init__(self, pub_date: str, title: str, body: str, author: User):
        self.title = title
        self.body = body
        self.author = author
        self.pub_date = pub_date

