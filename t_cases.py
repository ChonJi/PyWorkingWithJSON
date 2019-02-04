from mertics import Metrics

class TCases(Metrics):
    __custom__ = None
    __description__ = None
    __domain__ = None
    __hidden__ = None
    __id__ = None
    __key__ = None
    __n_ame__ = None
    __qualitative__ = None
    __type__ = None

tc = TCases()

for index, values in enumerate (tc.get_metrics()):
    print(values)

