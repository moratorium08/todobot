
class User:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def __repr__(self):
        ret = '{}:  {}'
        return ret.format(self.id, self.name)
