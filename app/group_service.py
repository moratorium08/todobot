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


def add_user_to_group(uid, gid):
    group_repo = app.get_group_repo()
    user_repo = app.get_user_repo()

    u = user_repo.find(uid)
    g = group_repo.find(gid)
    group_repo.add_user(g, u.id)


def list_group_users(gid):
    group_repo = app.get_group_repo()
    user_repo = app.get_user_repo()

    g = group_repo.find(gid)
    uids = group_repo.user_ids(g)

    users = []
    for uid in uids:
        u = user_repo.find(uid)
        users.append(u)

    return users
