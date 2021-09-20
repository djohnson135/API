#this is the database for the api
#Dictionary of key value pairs
Dict = {}

def test():
    print("test")

def PostDatabase(str, key):
    Dict[str] = key #add to database

def getDatabase(key):
    return Dict.get(key)

def PutDatabse():
    return
def PatchDatabase():
    return
def Delete(key):
    return