from iron_mq import *
ironmq = IronMQ(project_id="", token="")
queue = ironmq.queue("requests")

l = range(500000)
n = 3000
list_of_messages = [l[i:i+n] for i in range(0, len(l), n)]

for ls in list_of_messages:
    queue.post(*[str(i) for i in ls])
