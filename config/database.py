import pymongo

url = pymongo.MongoClient("mongodb://localhost:27017")

db = url["Employees"]

collection_name = db["Staff_Collection"]