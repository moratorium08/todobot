from domain import user
from repo.mongo import errors
from repo.mongo import mongo_repo


class UserRepo(mongo_repo.MongoRepo):
    kind = 'user'
    user_group_kind = 'user_group'

    ID = 'id'
    NAME = 'name'

    def __init__(self, db, user_group_dao):
        self.collection = db[self.kind]
        self.user_group_dao = user_group_dao

    def save(self, user):
        d = {self.ID: user.id,
             self.NAME: user.name}

        r = self.collection.insert_one(d)
        if not r.acknowledged:
            raise errors.SaveError

    def find(self, id_):
        ret = self.collection.find_one({self.ID: id_})
        if ret is None:
            raise errors.NotFound

        u = user.User(ret[self.ID], ret[self.NAME])
        return u

    def find_all(self):
        res = self.collection.find()
        ret = []
        for x in res:
            tmp = user.User(x[self.ID], x[self.NAME])
            ret.append(tmp)
        return ret

    def group_ids(self, user):
        ugs = self.user_group_dao.find_by_user_id(user.id)
        return [ug.group_id for ug in ugs]
