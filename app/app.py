from repo.mongo import group_repo
from repo.mongo import task_repo
from repo.mongo import user_repo
from repo.mongo import work_repo

_group_repo = None
_task_repo = None
_user_repo = None
_work_repo = None


def get_group_repo() -> group_repo.GroupRepo:
    if _group_repo is None:
        raise NotImplemented
    return _group_repo


def get_task_repo() -> task_repo.TaskRepo:
    if _task_repo is None:
        raise NotImplemented
    return _task_repo


def get_user_repo() -> user_repo.UserRepo:
    if _user_repo is None:
        raise NotImplemented
    return _user_repo


def get_work_repo() -> work_repo.WorkRepo:
    if _work_repo is None:
        raise NotImplemented
    return _work_repo


def set_group_repo(g: group_repo.GroupRepo):
    global _group_repo
    _group_repo = g


def set_task_repo(t: task_repo.TaskRepo):
    global _task_repo
    _task_repo = t


def set_user_repo(u: user_repo.UserRepo):
    global _user_repo
    _user_repo = u


def set_work_repo(w: work_repo.WorkRepo):
    global _work_repo
    _work_repo = w
