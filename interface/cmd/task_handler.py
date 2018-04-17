from datetime import datetime

from app import task_service


def menu():
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
