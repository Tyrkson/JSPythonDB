import json
import os

class Collection:
    def __init__(self, name, data):
        self.name = name
        self.data = data


def isCollectionExisting(name):
    for coll in collections:
        if coll["name"] == name:
            return True
    return False

def createNewCollection(name):
    newColl = Collection(name, [])
    addCollectionToList(newColl)

def addCollectionToList(coll):
    collections.append(coll.__dict__)

def testdb():
    return "See olen mina!"

def addElement(name, el):
    if isCollectionExisting(name) == False:
        createNewCollection(name)
    for coll in collections:
        if coll["name"] == name:
            coll["data"].append(el)
            break
    print(collections)
    saveCollections()
    return True #Returns success response when finished?

def getCollection(name):
    for coll in collections:
        if coll["name"] == name:
            return coll["data"]
    return False

def saveCollections():
    with open('data.json', 'w') as f:
        json.dump(collections, f)
    return True

def loadCollections():
    global collections
    if os.stat("data.json").st_size == 0:
        return False
    with open('data.json', 'r') as f:
        collections = json.load(f)

    return True

collections = []
loadCollections()
print(collections)
