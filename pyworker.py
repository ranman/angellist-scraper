import pymongo
import requests
from iron_mq import IronMQ
import os

mongo_url = os.getenv("MONGO_URL")
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")

project_id = os.getenv("IRON_PROJECT_ID")
token = os.getenv("IRON_TOKEN")

print token
# connect to mongo and choose a database
client = pymongo.MongoClient(mongo_url)
client.admin.authenticate(mongo_user, mongo_password)
db = client.angellist

# connect to ironmq and choose a queue
ironmq = IronMQ(project_id=project_id, token=token)
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
