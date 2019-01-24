import urllib.request
import json


class JSONProvider():
    __file_path__ = 'json/json_file.txt'

    def __init__(self):
        url = "https://sonarcloud.io/api/metrics/search?ps=10"
        urllib.request.urlretrieve(url, self.__file_path__)

    def get_json_file(self):
        json_file = open(self.__file_path__, 'r', encoding='utf-8')
        metrics = json.load(json_file)
        json_file.close()
        return metrics
