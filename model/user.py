class User:
    def __init__(self, _id: int, username: str):
        self._id = _id
        self.username = username

    def serialize(self):
        return {
            "_id": self._id,
            "username": self.username
        }
