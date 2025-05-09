# MongoDB connection
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["project_cv"]
collection = db["users"]