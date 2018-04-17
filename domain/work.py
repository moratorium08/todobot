import enum

from domain import task
from domain import user


class Work:
    class WorkStatus(enum.Enum):
        HIDDEN = 1
        PROGRESS = 2
        DONE = 3

    def __init__(self, task: task.Task, user: user.User, status: WorkStatus):
        self.task = task
        self.user = user
        self.status = status
