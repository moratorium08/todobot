from repo.mongo import mongo_repo

class UserRepo(mongo_repo.MongoRepo):
    kind = 'user'

    def __init__(self, db):
        self.collenction = db[self.kind]
