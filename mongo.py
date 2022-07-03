from pymongo import MongoClient
import os
import sys
import json

def readparameters():
    if(os.path.exists('parameters.json')):
        with open('parameters.json') as json_file:
            data = json.load(json_file)
            return data
client = MongoClient("mongodb+srv://admin:pbhat95@cluster0.duv1l.mongodb.net/?retryWrites=true&w=majority")
db = client["test"]
collection = db["test"]
results=collection.insert_one({"name":"manand"})
print(results.inserted_id)