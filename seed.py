from pymongo import MongoClient

#defines the database connection
client = MongoClient('mongodb://localhost:27017/')
db = client.torcrawl_db
collection = db.onions



#seeds your collection with an entry for the Tor Hidden Wiki
collection.insert_one({"address": "http://wiki5kauuihowqi5.onion", "timeout": 15, "attempts": 0})