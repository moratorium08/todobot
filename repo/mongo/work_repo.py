import typing

from domain import error
from domain import task
from domain import user
from domain import work
from repo.mongo import mongo_repo


class WorkRepo(mongo_repo.MongoRepo):
    kind = 'work'

    ID = 'id'
    TASK_ID = 'task_id'
    USER_ID = 'user_id'
    STATUS = 'status'

    def __init__(self, db):
        self.collection = db[self.kind]

    def save(self, w: work.Work):
        d = {self.ID: w.id,
             self.TASK_ID: w.task.id,
             self.USER_ID: w.user.id,
             self.STATUS: w.status.value}

        self.collection.find_one_and_update({self.ID: w.id},
                                            {'$set': d},
                                            upsert=True)

    def find_by_user(self,
                     user: user.User,
                     task_repo) -> typing.List[work.Work]:
        rets = self.collection.find({self.USER_ID: user.id})

        works = []
        for ret in rets:
            task = task_repo.find(ret[self.TASK_ID])
            w = work.Work(ret[self.ID],
                          task,
                          user,
                          work.Work.WorkStatus(ret[self.STATUS]))
            works.append(w)
        return works

    def find_by_user_and_task(self, t: task.Task, u: user.User) -> work.Work:
        ret = self.collection.find_one({self.USER_ID: u.id,
                                        self.TASK_ID: t.id})
        if ret is None:
            raise error.NoSuchWork

        w = work.Work(ret[self.ID],
                      t,
                      u,
                      work.Work.WorkStatus(ret[self.STATUS]))
        return w
