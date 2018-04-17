from app import group_service


def menu():
    print('何をしますか')
    print('[1] 追加')
    print('[2] 一覧')
    print('[3] グループを見る')
    print('[4] ユーザーをグループに追加')
    print('[5] グループに属するユーザーを表示')

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
    elif i == '4':
        print('ユーザーのIDは')
        uid = input()
        print('グループのIDは')
        gid = input()
        group_service.add_user_to_group(uid, gid)
    elif i == '5':
        print('グループのIDは')
        gid = input()
        users = group_service.list_group_users(gid)
        for j, user in enumerate(users):
            print('{}: {}'.format(j, user))
