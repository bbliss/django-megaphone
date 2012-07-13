import datetime
import redis
import json

from django.contrib.sites.models import Site
from django.db.models.loading import get_model
from django.core.cache import cache

from celery.decorators import task

@task(name='megaphone.send_announcement')
def send_announcement(announcement_id):
    Announcement = get_model('megaphone','Announcement')
    announcement = Announcement.objects.get(pk=announcement_id)

    channels = []
    for site in announcement.sites.all():
        channels.append('megaphone' + str(site.id))
        cache.set(str(site.id) + 'Megaphone', announcement.main_text, 60 * 60)

    msg = {'channels': channels, 'data': [announcement.main_text, announcement.pub_date]}
    server = redis.Redis()
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    server.publish('juggernaut', json.dumps(msg, default=dthandler))
