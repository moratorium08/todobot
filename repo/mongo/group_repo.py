import typing
import uuid


from domain import error
from domain import group
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
            raise error.NoSuchGroup

        g = group.Group(ret[self.ID], ret[self.NAME])
        return g

    def find_all(self) -> typing.List[group.Group]:
        res = self.collection.find()
        ret = []
        for x in res:
            tmp = group.Group(x[self.ID], x[self.NAME])
            ret.append(tmp)
        return ret

    def save(self, g: group.Group):
        d = {self.ID: g.id, self.NAME: g.name}
        self.collection.find_one_and_update({self.ID: g.id},
                                            {'$set': d},
                                            upsert=True)

    def add_user(self, g: group.Group, uid: str):
        self.user_group_dao.save(uuid.uuid1().hex, uid, g.id)

    def user_ids(self, g: group.Group) -> typing.List[str]:
        ugs = self.user_group_dao.find_by_group_id(g.id)
        return [ug.user_id for ug in ugs]
