from domain import error
from domain import task
from repo.mongo import mongo_repo


class TaskRepo(mongo_repo.MongoRepo):
    kind = 'task'

    ID = 'id'
    CONTENT = 'content'
    LIMIT = 'limit'

    def __init__(self, db):
        self.collection = db[self.kind]

    def find_all(self) -> [task.Task]:
        res = self.collection.find()
        ret = []
        for x in res:
            tmp = task.Task(x[self.ID], x[self.CONTENT], x[self.LIMIT])
            ret.append(tmp)
        return ret

    def save(self, t: task.Task):
        d = {self.ID: t.id,
             self.CONTENT: t.content,
             self.LIMIT: t.limit}

        r = self.collection.insert_one(d)
        if not r.acknowledged:
            raise error.NoSuchTask
