import enum

from domain import task
from domain import user


class Work:
    class WorkStatus(enum.Enum):
        HIDDEN = 1
        PROGRESS = 2
        DONE = 3

    def __init__(self,
                 id_: str,
                 task: task.Task,
                 user: user.User,
                 status: WorkStatus):
        self.id = id_
        self.task = task
        self.user = user
        self.status = status

    def __repr__(self) -> str:
        ret = '{}: {}'
        if self.status == self.WorkStatus.HIDDEN:
            status = '未公開'
        elif self.status == self.WorkStatus.PROGRESS:
            status = '進行中'
        elif self.status == self.WorkStatus.DONE:
            status = '完了'
        else:
            status = '未定義'

        return ret.format(self.task.content, status)

    def mark_as_done(self):
        self.status = self.WorkStatus.DONE
