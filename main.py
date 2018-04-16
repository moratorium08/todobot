import pymongo

import config

from app import app
from repo.mongo import group_repo
from repo.mongo import task_repo
from repo.mongo import user_repo
from repo.mongo import work_repo


def init():
    client = pymongo.MongoClient(config.mongo_url)
    db = client[config.database]

    app.group_repo = group_repo.GroupRepo(db)
    app.task_repo = task_repo.TaskRepo(db)
    app.user_repo = user_repo.UserRepo(db)
    app.work_repo = work_repo.WorkRepo(db)


def main():
    init()
