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
            coll["data"].append(json.loads(el))
            break
    print(collections)
    saveCollections()
    return True #Returns success response when finished?

def getUser(email):
    for coll in collections:
        if coll['name'] == 'Users':
            for i in coll['data']:
                if i['email'] == email:
                    return i
    return False

def checkUserCredentials(email, password):
    user = getUser(email)
    if user != False and user['password'] == password:
        return True
    else:
        return False

def updateUser(email):
    return True

def deleteCollections():
    global collections
    collections = []
    return open('data.json', 'w').close()

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
