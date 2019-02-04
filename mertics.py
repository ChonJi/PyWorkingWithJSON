import pandas as ps

from json_provider import JSONProvider
import pprint


class Metrics():
    __json_object__ = JSONProvider()
    __json___ = __json_object__.get_json_file()
    __metrics__ = __json___["metrics"]
    __p__ = __json___["p"]
    __ps__ = __json___["ps"]
    __total__ = __json___["total"]

    def __init__(self):
        pprint.pprint(self.__json___)

    def get_metrics(self):
        list = []
        for counter, value in enumerate(self.__metrics__):
            list.append(value)
        return list

    def get_p(self):
        return self.__p__

    def get_ps(self):
        return self.__ps__

    def get_total(self):
        return self.__total__

    def create_csv_file(self):
        flat = ps.read_json(self.__json___)
        ps.to_csv(flat)
