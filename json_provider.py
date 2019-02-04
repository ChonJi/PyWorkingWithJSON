import math
import urllib.request
import json
import pprint


class JSONProvider():
    __file_path__ = 'json/json_file.txt'

    def __init__(self):
        values = 500
        url = "https://sonarcloud.io/api/issues/search?componentKeys=ReportComparator&s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=500&pageIndex=1&organization=chonji-github&facets=severities%2Ctypes&additionalFields=_all"
        urllib.request.urlretrieve(url, self.__file_path__)
        json_file = open(self.__file_path__, 'r', encoding='utf-8')
        metrics = json.load(json_file)
        total = math.ceil(metrics["total"] / values) + 1
        for index in range(2, total, 1):
            url = f"https://sonarcloud.io/api/issues/search?componentKeys=ReportComparator&s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=500&pageIndex={index}&organization=chonji-github&facets=severities%2Ctypes&additionalFields=_all"
            with urllib.request.urlopen(url) as sjson:
                text = json.load(sjson)
                issues = str(text["issues"])
                with open(self.__file_path__, 'w+') as file:
                    file.write(issues)

    def get_json_file(self):
        json_file = open(self.__file_path__, 'r', encoding='utf-8')
        metrics = json.load(json_file)
        json_file.close()
        return metrics


jsonProvider = JSONProvider()
