

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

def testdb():
    return "See olen mina!"

def addElement(name, el):
    return None #Returns success response when finished?

def getCollection(name):
    return None #Returns the collection's data
