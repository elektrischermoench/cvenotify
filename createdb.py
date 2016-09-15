from pymongo import MongoClient
import json

client = MongoClient('localhost',27017)
database=client.vulns
mycollection=database.programs

with open('vulndb.json') as data:
   json_data = json.load(data)
   mycollection.insert_many(json_data)

