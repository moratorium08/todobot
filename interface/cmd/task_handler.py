from datetime import datetime

from app import task_service


def menu():
    print('何をしますか')
    print('[1] 追加')
    print('[2] 一覧')
    print('[3] UserにTaskを割り当て')
    print('[4] GroupにTaskを割り当て')
    print('[5] Userに割り当てられたTask表示')
    print('[6] Taskを完了')

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
    elif i == '2':
        tasks = task_service.list_tasks()
        for i, task in enumerate(tasks):
            print('{}: {}'.format(i, task))
    elif i == '3':
        print('TaskID')
        tid = input()
        print('UserID')
        uid = input()
        task_service.assign_task_to_user(tid, uid)
    elif i == '4':
        print('TaskID')
        tid = input()
        print('GroupID')
        gid = input()
        task_service.assign_task_to_group(tid, gid)
    elif i == '5':
        print('UserID')
        uid = input()
        works = task_service.list_user_assinged_works(uid)
        for i, w in enumerate(works):
            print('{}: {}'.format(i, w))
    elif i == '6':
        print('UserID')
        uid = input()
        print('TaskID')
        tid = input()
        task_service.complete_task(uid, tid)
