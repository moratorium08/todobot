from domain import group
from repo.mongo import errors
from repo.mongo import mongo_repo


class GroupRepo(mongo_repo.MongoRepo):
    kind = 'group'

    ID = 'id'
    NAME = 'name'

    def __init__(self, db):
        self.collenction = db[self.kind]

    def find(self, id_):
        ret = self.collenction.find_one({self.ID: id_})
        if ret is None:
            raise errors.NotFound

        g = group.Group(ret[self.ID], self.NAME)
        return g

    def save(self, g):
        d = {self.ID: g.id, self.NAME: g.name}
        r = self.collenction.insert_one(d)

        if not r.acknowledged:
            raise errors.SaveError


