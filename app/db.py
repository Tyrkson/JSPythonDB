

class Collection:
    def __init__(self, name, data):
        self.name = name
        self.data = data

collections = []


def createNewCollection(name):
    newColl = Collection(name, [])
    addCollectionToList(newColl)

def addCollectionToList(coll):
    collections.append(coll)
