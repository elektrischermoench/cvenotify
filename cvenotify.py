# cvenotify
#
# Kai Renken (code@koffeinsucht.de) 
#

from ares import CVESearch
from pymongo import MongoClient
import json
from smtplib import SMTP
import time

cve = CVESearch('http://localhost:5000/api')
client = MongoClient('localhost',27017)
database=client.vulns
mycollection=database.programs

def notifiy():
   to = 'foo@foo.bar'
   fro = 'cve-search@foo.bar'
   server = SMTP('adress',587)
   server.set_debuglevel(1)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login('user','pass')

   header = 'To:' + to + '\n' + 'From: ' + fro + '\n' + 'Subject:[CVE-Search] New Vulnerability ' + i['id']+'\n'
   msg = header + '\nhttp://localhost/cve/'+ i['id'] +'\n\n'
   server.sendmail(fro, to , msg.format(header))
   server.quit()
   #time.sleep(10) #needed if the MessageRateLimit is to small
   return
 
for entry in mycollection.find():
    queryresult = json.loads(cve.search(entry["vendor"]+'/'+entry["product"]+':'+entry["version"]).decode('utf-8'))
 
    # search all new cve's
    for i in queryresult:
       if (i['id'] != entry['lastcve']):
          notify()  
       else:
          break;
    
    # update db to last viewed cve
    if ((queryresult) and (queryresult[0]['id'] != entry["lastcve"])):
       mycollection.update({"_id":entry["_id"]}, {"$set": {"lastcve":queryresult[0]['id']} })
