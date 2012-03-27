import datetime
import redis
import json

from celery.decorators import task

@task(name='megaphone.delayed_announcement')
def delayed_announcement(msg):
    server = redis.Redis()
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    server.publish('juggernaut', json.dumps(msg, default=dthandler))
