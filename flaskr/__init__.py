#!/usr/bin/python3
# -*- coding: latin-1 -*-
import os
import sys
# import psycopg2
import json
from bson import json_util
from pymongo import MongoClient
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

# REPLACE WITH YOUR DATABASE NAME
MONGODATABASE = "my_db"
MONGOSERVER = "localhost"
MONGOPORT = 27017
client = MongoClient(MONGOSERVER, MONGOPORT)
mongodb = client[MONGODATABASE]

''' # Uncomment for postgres connection
# REPLACE WITH YOUR DATABASE NAME, USER AND PASS
POSTGRESDATABASE = "mydatabase"
POSTGRESUSER = "grupo12"
POSTGRESPASS = "grupo12"
postgresdb = psycopg2.connect(
    database=POSTGRESDATABASE,
    user=POSTGRESUSER,
    password=POSTGRESPASS)
'''

#Cambiar por Path Absoluto en el servidor
QUERIES_FILENAME = '/var/www/flaskr/queries'


@app.route("/")
def home():
    with open(QUERIES_FILENAME, 'r', encoding='utf-8') as queries_file:
        json_file = json.load(queries_file)
        pairs = [(x["name"],
                  x["database"],
                  x["description"],
                  x["query"]) for x in json_file]
        return render_template('file.html', results=pairs)


@app.route("/mongo")
def mongo():
    query = request.args.get("query")
    results = eval('mongodb.'+query)
    results = json_util.dumps(results, sort_keys=True, indent=4)
    if "find" in query:
        return render_template('mongo.html', results=results)
    else:
        return "ok"

@app.route("/mongo_fecha")
def fecha():
    query = request.args.get("query")
    query = "escuchas.find({{'fecha':'{0}'}})".format(query)
    results = eval('mongodb.'+query)
    results = json_util.dumps(results, sort_keys=True, indent=4)
    return render_template('mongo.html', results=results)

@app.route("/mongo_numero")
def numero():
    query = request.args.get("query")
    number, quantity = query.split(",")
    query = "escuchas.find({{'numero':'{0}'}},{{'_id':1,'contenido':1,'fecha':1,'numero':1,'ciudad':1}}).sort('fecha',-1).limit({1})".format(number, quantity)
    results = eval('mongodb.' + query)
    results = json_util.dumps(results, sort_keys=True, indent=4)
    return render_template('mongo.html', results=results)

@app.route("/mongo_clave")
def clave():
    query = request.args.get("query")
    query = "escuchas.find({{'$text':{{'$search':'{}'}},{{'_id':1,'contenido':1,'fecha':1,'numero':1,'ciudad':1}})".format(query)
    results = eval('mongodb.' + query)
    results = json_util.dumps(results, sort_keys=True, indent=4)
    return render_template('mongo.html', results=results)

@app.route("/postgres")
def postgres():
    query = request.args.get("query")
    cursor = postgresdb.cursor()
    cursor.execute(query)
    results = [[a for a in result] for result in cursor]
    print(results)
    return render_template('postgres.html', results=results)


@app.route("/example")
def example():
    return render_template('file.html')


if __name__ == "__main__":
    app.run()
