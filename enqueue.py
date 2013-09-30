from iron_worker import *
worker = IronWorker()
task = worker.queue(code_name="startup")
print task
