# cvenotify
#
# Kai Renken (kai@koffeinsucht.de) 
#

from ares import CVESearch
from pymongo import MongoClient
import json

cve = CVESearch('http://localhost:5000/api')
client = MongoClient('localhost',27017)
database=client.vulns
mycollection=database.programs

for entry in mycollection.find():
    queryresult = json.loads(cve.search(entry["vendor"]+'/'+entry["product"]+':'+entry["version"]).decode('utf-8'))
    
    # search all new cve's
    for i in queryresult:
       if (i['id'] != entry['lastcve']):
          print(i['id']) #TODO create bugticket
       else:
          break;
    
    # update db to last viewed cve
    if ((queryresult) and (queryresult[0]['id'] != entry["lastcve"])):
       mycollection.update({"_id":entry["_id"]}, {"$set": {"lastcve":queryresult[0]['id']} })
