from repo.mongo import errors


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

    def find_by_user_id(self, uid):
        rets = self.collection.find({self.USER_ID: uid})
        if rets is None:
            raise errors.NotFound

        ugs = []
        for ret in rets:
            ug = UserGroup(ret[self.ID], ret[self.USER_ID], ret[self.GROUP_ID])
            ugs.append(ug)
        return ugs
