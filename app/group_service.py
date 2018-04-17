from app import app
from domain import group


def add_group(gid, name):
    group_repo = app.get_group_repo()
    g = group.Group(gid, name)
    group_repo.save(g)


def list_groups():
    group_repo = app.get_group_repo()
    return group_repo.find_all()


def get_group(gid):
    group_repo = app.get_group_repo()
    g = group_repo.find(gid)
    return g
