
class ArgumentException(Exception):
    detail = '処理に失敗しました'


class NoSuchGroup(ArgumentException):
    detail = 'そのようなGroupが存在しませんでした'


class NoSuchTask(ArgumentException):
    detail = 'そのようなTaskが存在しませんでした'


class NoSuchUser(ArgumentException):
    detail = 'そのようなUserが存在しませんでした'


class NoSuchWork(ArgumentException):
    detail = 'そのようなWorkが存在しませんでした'


class PersistentException(ArgumentException):
    detail = 'データベースとの通信に失敗しました'
