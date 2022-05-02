class DbConfig:
    userName = "user-01"
    passWord = "dm8ONKwtiZQA7Vpc"
    url = "mongodb+srv://{username}:{password}@cluster0.laopn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(username=userName,password=passWord)

    # url = "mongodb+srv://{username}:{password}@cluster0.laopn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(username=userName,password=passWord)
    # url = "mongodb+srv://cluster0.laopn.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

