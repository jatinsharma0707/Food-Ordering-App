import json

def setFood(List):
    fp = open("food.json",'w')
    data = json.dumps(List)
    fp.write(data)
    fp.close()

def getFood():
    fp = open("food.json")
    content = fp.read()
    fp.close()
    itemList = json.loads(content)
    return itemList

def setUser(List):
    fp = open("users.json",'w')
    data = json.dumps(List)
    fp.write(data)
    fp.close()

def getUser():
    fp = open("users.json")
    content = fp.read()
    fp.close()
    itemList = json.loads(content)
    return itemList
