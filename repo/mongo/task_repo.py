from repo.mongo import mongo_repo

class TaskRepo(mongo_repo.MongoRepo):
    kind = 'task'

    def __init__(self, db):
        self.collenction = db[self.kind]
