from json_provider import JSONProvider


class Metrics():
    __json_object__ = JSONProvider()
    __metrics__ = __json_object__.get_json_file()

    def print_metrics(self):
        print(self.__metrics__)


if __name__ == "__main__":
    m = Metrics()
    m.print_metrics()
