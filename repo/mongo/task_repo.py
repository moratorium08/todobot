from domain import task
from repo.mongo import errors
from repo.mongo import mongo_repo

class TaskRepo(mongo_repo.MongoRepo):
    kind = 'task'

    ID = 'id'
    CONTENT = 'content'
    LIMIT = 'limit'

    def __init__(self, db):
        self.collenction = db[self.kind]

    def find_all(self):
        ret = self.collenction.find()
        l = []
        for x in ret:
            tmp = task.Task(x[self.ID], x[self.CONTENT], x[self.LIMIT])
            l.append(tmp)
        return l

    def save(self, t):
        d = {self.ID: t.id,
             self.CONTENT: t.content,
             self.LIMIT: t.limit}

        r = self.collenction.insert_one(d)
        if not r.acknowledged:
            raise errors.SaveError

