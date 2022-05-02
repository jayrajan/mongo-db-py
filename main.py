import pymongo as pym
import config.DbConfig as config


# Connect to mongodb

try:
    db = config.DbConfig()
    client = pym.MongoClient(db.url)
    print(client.server_info())
except pym.errors.ServerSelectionTimeoutError as err:
    print(err)


# schema


# Disconnect from mongodb
client.close()