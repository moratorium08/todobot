
class User:
    def __init__(self, id_: str, name: str):
        self.id = id_
        self.name = name

    def __repr__(self) -> str:
        ret = '{}:  {}'
        return ret.format(self.id, self.name)
