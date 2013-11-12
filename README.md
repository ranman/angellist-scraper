## Synopsis

grab all the data from angellist and home they don't sue me.

## Code Example

nope.

## Motivation

I'm not sure... Sometimes I decide to program things

## Installation

Change these lines in `pyworker.py`:

```python
client = pymongo.MongoClient('mongodb.random.com')
client.admin.authenticate('', '')
```
and these in `pyq.py`:

```python
ironmq = IronMQ(project_id="", token="")
queue = ironmq.queue("requests")
```

Then do this:

```shell
$ gem install iron_worker_ng
$ iron_worker upload startup.worker
$ python pyq.py
$ repeat 500 python enqueue.py
```

That last line starts up 500 workers that will ask for 1000 ids at a time for the next few hours.

Apparently you don't have to do this anymore you can just do:

```shell
$ repeat 500 iron_worker queue startup.worker --timeout 3600
```

## Contributors

I welcome you.

## License

I have no idea what licensing is but feel free to use this code without any warranty or liability.