# coding: utf-8
import pymongo

from app import app
import config
from interface.cmd import cmd
from repo.mongo import group_repo
from repo.mongo import task_repo
from repo.mongo import user_repo
from repo.mongo import user_group_dao
from repo.mongo import work_repo


def init():
    client = pymongo.MongoClient(config.mongo_url)
    db = client[config.database]

    ug_dao = user_group_dao.UserGroupDao(db)
    app.set_group_repo(group_repo.GroupRepo(db, ug_dao))
    app.set_task_repo(task_repo.TaskRepo(db))
    app.set_user_repo(user_repo.UserRepo(db, ug_dao))
    app.set_work_repo(work_repo.WorkRepo(db))


def main():
    init()
    ret = True
    while ret:
        ret = cmd.main_menu()


main()
