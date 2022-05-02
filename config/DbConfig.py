import pymongo

class DbConfig:
    userName = "user-01"
    passWord = "dm8ONKwtiZQA7Vpc"
    url = "mongodb+srv://{username}:{password}@cluster0.laopn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(username=userName,password=passWord)



