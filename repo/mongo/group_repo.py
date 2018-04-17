from domain import group
from repo.mongo import errors
from repo.mongo import mongo_repo


class GroupRepo(mongo_repo.MongoRepo):
    kind = 'group'

    ID = 'id'
    NAME = 'name'

    def __init__(self, db, user_group_dao):
        self.collection = db[self.kind]
        self.user_group_dao = user_group_dao

    def find(self, id_: str) -> group.Group:
        ret = self.collection.find_one({self.ID: id_})
        if ret is None:
            raise errors.NotFound

        g = group.Group(ret[self.ID], self.NAME)
        return g

    def find_all(self) -> [group.Group]:
        res = self.collection.find()
        ret = []
        for x in res:
            tmp = group.Group(x[self.ID], x[self.NAME])
            ret.append(tmp)
        return ret

    def save(self, g: group.Group):
        d = {self.ID: g.id, self.NAME: g.name}
        r = self.collection.insert_one(d)

        if not r.acknowledged:
            raise errors.SaveError

    def user_ids(self, g: group.Group):
        ugs = self.user_group_dao.find_by_group_id(g.id)
        return [ug.user_ids for ug in ugs]
