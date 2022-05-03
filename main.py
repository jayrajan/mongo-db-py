import pymongo as pym
import config.DbConfig as config


# Connect to mongodb

try:
    dbConfig = config.DbConfig()
    client = pym.MongoClient(dbConfig.url)
    print("Conenction to MongoDb Established")
    # print(client.server_info())
except pym.errors.ServerSelectionTimeoutError as err:
    print(err)

# create a database called Users
db = client.users

# data
firstName = ["jay","ed","abi","sherin","aaron","steven"]
secondName = ["r","w","w","a","a","l"]
age = [22,33,22,14,6,3]

for i in range(len(firstName)):
    users = {
        "firstName" : firstName[i],
        "secondName" : secondName[i],
        "age" : age[i]
    }
    # insert users into a collection called 
    # Putting users data
    result = db.users.insert_one(users)

print("User data added to the collection")

# CRUD operations

# READ
# def read_db(db):
read = db.users.find({"firstName":"jay"})
for items in read:
    print(items['_id'])





# Disconnect from mongodb
client.close()
print("Connection to mongoDb Disconnected")

