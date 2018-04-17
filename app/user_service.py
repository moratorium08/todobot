from app import app
from domain import user


def add_user(uid, name):
    user_repo = app.get_user_repo()
    u = user.User(uid, name)
    user_repo.save(u)


def list_users():
    user_repo = app.get_user_repo()
    return user_repo.find_all()


def get_user(uid):
    user_repo = app.get_user_repo()
    u = user_repo.find(uid)
    return u
