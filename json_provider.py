import math
import urllib.request
import json
import pprint


class JSONProvider():
    __file_path__ = 'json/json_file.json'

    def __init__(self):
        values = 500
        data_collection = []
        first_request = urllib.request.urlopen(self.get_url(1))
        metrics = json.load(first_request)
        number_of_issues = metrics["total"]
        data_collection.append(metrics)
        total_runs = math.ceil(number_of_issues / values) + 1
        for index in range(2, total_runs, 1):
            request = urllib.request.urlopen(self.get_url(index))
            metrics = json.load(request)
            data_collection.append(metrics)
        with open(self.__file_path__, 'w') as file:
            json.dump(data_collection, file, sort_keys=True, indent=2)

    def get_url(self, index):
        return (
            f"https://sonarcloud.io/api/issues/search?componentKeys=ReportComparator&s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=1&pageIndex={index}"
            "&organization=chonji-github&facets=severities%2Ctypes&additionalFields=_all")

    def create_csv(self):
        issues_dict = []
        input_open = json.loads(open(self.__file_path__).read())
        pprint.pprint(input_open)

        # issues = [issue["issues"] for issue in input_open]
        # issues = input_open["issues"]
        # flows = issues[0]["flows"]
        # pprint.pprint(issues)




jsonProvider = JSONProvider()
jsonProvider.create_csv()
