import json

dir="./CONFIG/"
class conf:
    def __init__(self, user, spotify):
        self.user = user
        self.spotify = spotify

CONFIG=conf()
conf_dict = json.loads((open(dir+"Default.json", "r")).read())
CONFIG= conf(**conf_dict)

def getConfig():
    return CONFIG