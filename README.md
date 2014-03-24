## Synopsis

Put the Angellist startups into MongoDB using a Iron.io queue and python.

## Code Example

nope.

## Motivation

Sometimes Randall programs things and I try to fix them.

## Installation

Set the follow environment variables

* MONGO_URL- url to your mongoDB instance
* MONGO_USER - user for mongoDB instance
* MONGO_PASSWORD - password for above user
* IRON_PROJECT_ID- IRON_MQ project ID
* IRON_TOKEN - IRON_MQ project token

Install the python environment
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
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
