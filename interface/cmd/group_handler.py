from app import group_service


def menu():
    print('何をしますか')
    print('[1] 追加')
    print('[2] 一覧')
    print('[3] グループを見る')

    i = input()
    if i == '1':
        print('グループ名は')
        name = input()
        print('IDは')
        id_ = input()

        group_service.add_group(id_, name)
    elif i == '2':
        groups = group_service.list_groups()
        for i, group in enumerate(groups):
            print('{}: {}'.format(i, group))
    elif i == '3':
        print('IDは')
        id_ = input()
        group = group_service.get_group(id_)
        print(group)
