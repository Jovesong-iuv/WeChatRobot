# -*- coding: utf-8 -*-
"""
@author: Joker_iuv(文歌属予,琴瑟嘉棋)
@contact: lmwiuv@163.com
@file: func_gdtq
@time: 2024/4/21 01:08
@ide: PyCharm
@desc:
"""


class Gdtq:
    def __init__(self, conf: dict) -> None:
        self.api_key = conf.get("api_key")
        self.converstion_list = {}

    @staticmethod
    def value_check(conf: dict) -> bool:
        if conf and conf.get("api_key"):
            return True
        return False

    def __repr__(self):
        return "Gdtq"


if __name__ == "__main__":
    from configuration import Config

    config = Config().GDTQ
    if not config:
        exit(0)

    gdtq = Gdtq(config)
