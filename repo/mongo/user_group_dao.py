import typing
from domain import error


class UserGroup:
    def __init__(self, id_, uid, gid):
        self.id = id_
        self.user_id = uid
        self.group_id = gid


class UserGroupDao:
    kind = 'user_group'

    ID = 'id'
    USER_ID = 'user_id'
    GROUP_ID = 'group_id'

    def __init__(self, db):
        self.collection = db[self.kind]

    def find_by_user_id(self, uid: str) -> typing.List[UserGroup]:
        rets = self.collection.find({self.USER_ID: uid})

        ugs = []
        for ret in rets:
            ug = UserGroup(ret[self.ID], ret[self.USER_ID], ret[self.GROUP_ID])
            ugs.append(ug)
        return ugs

    def find_by_group_id(self, gid: str) -> typing.List[UserGroup]:
        rets = self.collection.find({self.GROUP_ID: gid})

        ugs = []
        for ret in rets:
            ug = UserGroup(ret[self.ID], ret[self.USER_ID], ret[self.GROUP_ID])
            ugs.append(ug)
        return ugs

    def save(self, id_: str, uid: str, gid: str):
        d = {self.ID: id_,
             self.USER_ID: uid,
             self.GROUP_ID: gid}

        r = self.collection.insert_one(d)
        if not r.acknowledged:
            raise error.PersistentException
