from app import user_service


def menu():
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
