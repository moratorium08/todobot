# coding: utf-8
from datetime import datetime

import pymongo


from app import app
from app import task_service
import config
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


def menu():
    print('何をしますか')
    print('[1] Task')
    print('[q] Quit')

    i = input()
    if i == '1':
        task()
    elif i == 'q':
        return False
    return True

def main():
    init()
    ret = True
    while ret:
        ret = menu()
main()



