# coding: utf-8
from datetime import datetime


class Task:
    def __init__(self, id_: str, content: str, limit: datetime):
        self.id = id_
        self.content = content
        self.limit = limit

    def __repr__(self):
        ret = '{} を {} までに'
        return ret.format(self.content, self.get_str_limit())

    def get_str_limit(self) -> str:
        return self.limit.strftime("%Y/%m/%d %H:%M")
