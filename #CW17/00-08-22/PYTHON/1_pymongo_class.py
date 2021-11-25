from pymongo import MongoClient
import pprint

client = MongoClient("localhost", 27017)

# print(client.list_database_names())

# db = client.test1
# print(db)

# print(db.list_collections)

# print(db.list_collection_names())

# collection = db.empDetails

# print(collection)

# for i in collection.find():
#     pprint.pprint(i)
#     print("__________")
