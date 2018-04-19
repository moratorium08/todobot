import typing

from domain import error
from domain import user
from repo.mongo import mongo_repo


class UserRepo(mongo_repo.MongoRepo):
    kind = 'user'
    user_group_kind = 'user_group'

    ID = 'id'
    NAME = 'name'

    def __init__(self, db, user_group_dao):
        self.collection = db[self.kind]
        self.user_group_dao = user_group_dao

    def save(self, user: user.User):
        d = {self.ID: user.id,
             self.NAME: user.name}

        self.collection.find_one_and_update({self.ID: user.id},
                                            {'$set': d},
                                            upsert=True)

    def find(self, id_: str) -> user.User:
        ret = self.collection.find_one({self.ID: id_})
        if ret is None:
            raise error.NoSuchUser

        u = user.User(ret[self.ID], ret[self.NAME])
        return u

    def find_all(self) -> typing.List[user.User]:
        res = self.collection.find()
        ret = []
        for x in res:
            tmp = user.User(x[self.ID], x[self.NAME])
            ret.append(tmp)
        return ret

    def group_ids(self, user: user.User) -> typing.List[str]:
        ugs = self.user_group_dao.find_by_user_id(user.id)
        return [ug.group_id for ug in ugs]
