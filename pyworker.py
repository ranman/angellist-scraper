import pymongo
import requests
from iron_mq import *
client = pymongo.MongoClient('mercury.ranman.org')
client.admin.authenticate('', '')
db = client.angellist
ironmq = IronMQ(project_id="", token="")
queue = ironmq.queue("requests")

reqs = []
i = 0
max_reqs = 1000
while True:
    q = queue.get()['messages'][0]
    r = requests.get('http://api.angel.co/1/startups/{0}'.format(q['body'])).json()
    if not r.get('error'):
        reqs.append(r)
        queue.delete(q['id'])
        print q['body']
    elif r.get('error') == "over_limit":
        print i
        break
    if r.get('error'):
        queue.delete(q['id'])
    elif i > max_reqs:
        break
    i += 1

if len(reqs) > 0:
    db.startups.insert(reqs)
