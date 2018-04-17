from repo.mongo import mongo_repo


class WorkRepo(mongo_repo.MongoRepo):
    kind = 'work'

    def __init__(self, db):
        self.collection = db[self.kind]
