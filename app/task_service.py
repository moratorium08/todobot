import uuid

from app import app
from domain import task
from domain import work


def add_task(content, limit):
    task_repo = app.get_task_repo()
    g = task.Task(uuid.uuid1().hex, content, limit)
    task_repo.save(g)


def list_tasks():
    task_repo = app.get_task_repo()
    return task_repo.find_all()


def assign_task_to_group(task_id, group_id):
    group_repo = app.get_group_repo()
    task_repo = app.get_task_repo()
    user_repo = app.get_user_repo()
    work_repo = app.get_work_repo()

    task = task_repo.find(task_id)
    g = group_repo.find(group_id)
    user_ids = group_repo.user_ids(g)

    for user_id in user_ids:
        user = user_repo.find(user_id)
        w = work.Work(uuid.uuid1().hex,
                      task,
                      user,
                      work.Work.WorkStatus.PROGRESS)
        work_repo.save(w)


def assign_task_to_user(task_id, user_id):
    task_repo = app.get_task_repo()
    user_repo = app.get_user_repo()
    work_repo = app.get_work_repo()

    task = task_repo.find(task_id)
    user = user_repo.find(user_id)
    w = work.Work(uuid.uuid1().hex,
                  task,
                  user,
                  work.Work.WorkStatus.PROGRESS)
    work_repo.save(w)


def list_user_assinged_works(user_id):
    task_repo = app.get_task_repo()
    user_repo = app.get_user_repo()
    work_repo = app.get_work_repo()

    user = user_repo.find(user_id)
    return work_repo.find_by_user(user, task_repo)


def complete_task(user_id, task_id):
    task_repo = app.get_task_repo()
    user_repo = app.get_user_repo()
    work_repo = app.get_work_repo()

    task = task_repo.find(task_id)
    user = user_repo.find(user_id)

    w = work_repo.find_by_user_and_task(task, user)
    w.mark_as_done()
    work_repo.save(w)
