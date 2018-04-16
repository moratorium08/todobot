import uuid

from app import app
from domain import task


def add_task(content, limit):
    task_repo = app.task_repo
    g = task.Task(uuid.uuid1().hex, content, limit)
    task_repo.save(g)

def list_tasks():
    task_repo = app.task_repo
    l = task_repo.find_all()
    return l
