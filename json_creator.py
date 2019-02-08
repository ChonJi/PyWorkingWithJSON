import datetime

import unicodecsv as csv
import urllib.request
import json
import pprint


class JSONCreator():
    __JSON_FILE_PATH = 'json/json_file.json'
    __CSV_FILE_PATH = 'csv/file.csv'
    __REQ_MAX_SIZE = 500

    def __init__(self):
        self._data = {}
        self.get_data_to_json()
        with open(self.__JSON_FILE_PATH, 'w') as file:
            json.dump(self._data, file, sort_keys=True, indent=2)

    def get_data_to_json(self):
        index = 1
        issues_current = 0
        issues_total = 0
        while (True):
            response_json = json.load(urllib.request.urlopen(self.get_url(index)))

            if index == 1:
                issues_total = response_json['total'] + self.__REQ_MAX_SIZE

            issues_current += self.__REQ_MAX_SIZE

            if issues_current > issues_total or issues_total == 0:
                break

            for key, value in response_json.items():
                if key in self._data:
                    if type(self._data[key]) is list:
                        self._data[key].extend(value)
                    elif type(self._data[key]) is int:
                        self._data[key] += value
                    elif type(self._data[key]) is dict:
                        if key in ['paging']:
                            pass
                        else:
                            raise KeyError(f"This key {key} is not yet supported")
                    else:
                        raise TypeError(f"This type {type(self._data[key])} is not supported yet"
                                        f" for key: {key}")
                else:
                    self._data[key] = value

    def get_url(self, index):
        return (
            f"https://sonarcloud.io/api/issues/search?componentKeys=ReportComparator&s=FILE_LINE&resolved=false&types=CODE_SMELL&ps=1&pageIndex={index}"
            "&organization=chonji-github&facets=severities%2Ctypes&additionalFields=_all")

    def create_csv(self):
        # with open(self.__JSON_FILE_PATH, 'r') as json_file:
        #     data = json.load(json_file)
        # components = data['components']
        # facets = data['facets']
        #
        #
        # project_name = 'Project name: ' + components[1]['key']
        # debt_total = 'Debt total: ' + str(data['debtTotal'])
        # print(project_name)
        #
        # with open(self.__CSV_FILE_PATH, 'wb') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerow([project_name, debt_total])
        #     writer.writerow(['Severity', 'Number'])
        #     checker = ''
        #     for values in facets:
        #         for val in values['values']:
        #             if val['val'] in checker:
        #                 break
        #             writer.writerow([val['val'],str(val['count'])])
        #             checker = checker + val['val']
        #     # writer.writerow()

        import csv
        project_name = self._data['components'][1]['key']
        issues = self._data['issues']

        with open(f'csv/{project_name}.csv', 'w', newline='') as new_csv:
            headers = ['Component', 'Message', 'Start Line', 'End Line', 'Debt', 'Effort']
            writer = csv.DictWriter(new_csv, fieldnames=headers)
            writer.writeheader()
            for issue in issues:
                for flow in issue['flows']:
                    for text in flow['locations']:
                        writer.writerow({'Component' : issue['component'], 'Message' : text['msg'], 'Start Line' : text['textRange']['startLine'], 'End Line' : text['textRange']['endLine'], 'Debt' : issue['debt'], 'Effort' : issue['effort']})


create = JSONCreator()
create.create_csv()
