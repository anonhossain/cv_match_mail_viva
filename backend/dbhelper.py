# MongoDB connection
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CVProject"]
collection = db["registration"]