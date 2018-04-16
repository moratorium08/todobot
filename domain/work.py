import enum

class Work:
    class WorkStatus(enum.Enum):
        HIDDEN = 1
        PROGRESS = 2
        DONE = 3

    def __init__(self, task, user, status):
        self.task = task
        self.user = user
        self.status = status


