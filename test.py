from bson import json_util
from pymongo import MongoClient


MONGODATABASE = "my_db"
MONGOSERVER = "localhost"
MONGOPORT = 27017
client = MongoClient(MONGOSERVER, MONGOPORT)
mongodb = client[MONGODATABASE]

if __name__ == "__main__":
    query = input()
    results = eval('mongodb.' + query)
    results = json_util.dumps(results, sort_keys=True, indent=4)
    print(results)