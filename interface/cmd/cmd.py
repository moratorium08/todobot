from domain import error
from interface.cmd import group_handler
from interface.cmd import task_handler
from interface.cmd import user_handler


def main_menu():
    print('何をしますか')
    print('[1] Task')
    print('[2] User')
    print('[3] Group')
    print('[q] Quit')

    i = input()
    try:
        if i == '1':
            task_handler.menu()
        elif i == '2':
            user_handler.menu()
        elif i == '3':
            group_handler.menu()
        elif i == 'q':
            return False
    except error.ArgumentException as e:
        print(e.detail)

    return True
