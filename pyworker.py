import pymongo
import requests
from iron_mq import IronMQ

# connect to mongo and choose a database
client = pymongo.MongoClient('mongodb.random.com')
client.admin.authenticate('', '')
db = client.angellist

# connect to ironmq and choose a queue
ironmq = IronMQ(project_id="", token="")
queue = ironmq.queue("requests")
url = 'http://api.angel.co/1/startups/{0}'
#
results = []
i = 0
max_reqs = 1000
while True:
    message = queue.get()['messages'][0] # grab the "id" to use
    r = requests.get(url.format(message['body'])).json()
    if not r.get('error'):
        results.append(r)
        # remove from queue since it was successful
        queue.delete(message['id'])
        print(message['body'])
    elif r.get('error') == "over_limit":
        # if we go over our limit then stop trying to get more
        print(i)
        break
    if r.get('error'):
        # if there is another kind of error then just forget about it
        queue.delete(message['id'])
    elif i > max_reqs:
        break
    i += 1

if len(results) > 0:
    db.startups.insert(results)
