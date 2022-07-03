from http import client
from pymongo import MongoClient
import os
import json

def read_parameters():
    if(os.path.exists('parameters.json')):
        with open('parameters.json') as json_file:
            data = json.load(json_file)
            return data

def mongo_client():
    USERNAME = read_parameters()["username"]
    PASSWORD = read_parameters()["password"]
    SRV_STRING="mongodb+srv://{}:{}@cluster0.duv1l.mongodb.net/?retryWrites=true&w=majority".format(USERNAME,PASSWORD)
    client = MongoClient(SRV_STRING)
    return client

def find_in_mongo(query,db,collection):
    mongoclient=mongo_client()
    db=mongoclient[db]
    collection=db[collection]
    return collection.find(query)


def insert_in_mongo(query,db,collection):
    mongoclient=mongo_client()
    db=mongoclient[db]
    collection=db[collection]
    collection.insert_one(query)
    return True

def delete_in_mongo(query,db,collection):
    mongoclient=mongo_client()
    db=mongoclient[db]
    collection=db[collection]
    collection.delete_one(query)
    return True

def delete_many_in_mongo(query,db,collection):
    mongoclient=mongo_client()
    db=mongoclient[db]
    collection=db[collection]
    collection.delete_many(query)
    return True