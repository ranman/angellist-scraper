from iron_worker import IronWorker
worker = IronWorker()
task = worker.queue(code_name="startup")
print(task)
