import json


def jsonHandling(path):
    with open(path) as data:
        finalData = json.load(data)
        return finalData
