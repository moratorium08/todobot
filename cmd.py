# coding: utf-8
from datetime import datetime

import pymongo


from app import app
from app import task_service
from app import user_service
import config
from repo.mongo import group_repo
from repo.mongo import task_repo
from repo.mongo import user_repo
from repo.mongo import user_group_dao
from repo.mongo import work_repo


def init():
    client = pymongo.MongoClient(config.mongo_url)
    db = client[config.database]

    app.group_repo = group_repo.GroupRepo(db)
    app.task_repo = task_repo.TaskRepo(db)
    app.user_repo = user_repo.UserRepo(db, user_group_dao)
    app.work_repo = work_repo.WorkRepo(db)


def task():
    print('何をしますか')
    print('[1] 追加')
    print('[2] 一覧')

    i = input()
    if i == '1':
        print('内容は?')
        content = input()
        print('期限は？(形式: 201801011200')
        limit = input()

        try:
            limit = datetime.strptime(limit, '%Y%m%d%H%M')
        except Exception:
            print('時間のパースに失敗しました')
            return
        task_service.add_task(content, limit)
    else:
        tasks = task_service.list_tasks()
        for i, task in enumerate(tasks):
            print('{}: {}'.format(i, task))

def user():
    print('何をしますか')
    print('[1] 追加')
    print('[2] 一覧')
    print('[3] ユーザーを指定して表示')

    i = input()
    if i == '1':
        print('ユーザー名は？')
        name = input()
        print('ユーザーIDは？')
        id_ = input()
        user_service.add_user(id_, name)
    elif i == '2':
        users = user_service.list_users()
        for i, user in enumerate(users):
            print('{}: {}'.format(i, user))
    else:
        print('ユーザーIDは？')
        uid = input()
        user = user_service.get_user(uid)
        print(user)

def menu():
    print('何をしますか')
    print('[1] Task')
    print('[2] User')
    print('[q] Quit')

    i = input()
    if i == '1':
        task()
    elif i == '2':
        user()
    elif i == 'q':
        return False
    return True

def main():
    init()
    ret = True
    while ret:
        ret = menu()
main()



