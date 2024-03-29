from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, foto, plan="", credits="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.credits = credits
        self.plan = plan
        self.foto = foto

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)


class Item():
    def __init__(self, name, type, cap, status, link) -> None:
        self.name = name
        self.type = type
        self.cap = cap
        self.status = status
        self.link = link
