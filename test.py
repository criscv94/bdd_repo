#from bson import json_util
#from pymongo import MongoClient

MONGODATABASE = "my_db"
MONGOSERVER = "localhost"
MONGOPORT = 27017
#client = MongoClient(MONGOSERVER, MONGOPORT)
#mongodb = client[MONGODATABASE]

if __name__ == "__main__":
    query = "20160625, 10"
    numero, cantidad = query.replace(" ","").split(",")
    print(numero, cantidad)
    results = "escuchas.find({{'$text':{{'$search':'{0}'}},{{'_id':1,'contenido':1,'fecha':1,'numero':1,'ciudad':1}})".format(numero)
    #results = eval('mongodb.' + query)
    #results = json_util.dumps(results, sort_keys=True, indent=4)
    print(results)