from model.user import User
from datetime import datetime
class Post:
    def __init__(self, _id: int, title: str, text: str, published: datetime, author: User):
        self._id = _id
        self.title = title
        self.text = text
        self.published = published
        self.author = author

    def serialize(self):
        return {
            "_id": self._id,
            "title": self.title,
            "text": self.text,
            "published": self.published,
            "author": self.author.serialize()
        }

