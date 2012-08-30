import datetime
import redis
import json

from django.contrib.sites.models import Site
from django.db.models.loading import get_model
from django.core.cache import cache
from django.conf import settings

from celery.decorators import task

def _get_juggernaut_server():
    server_settings = getattr(settings, 'NOWPLAYING_JUGGERNAUT_SERVER', {})
    host = server_settings.get('host', 'localhost')
    port = server_settings.get('port', 6379)
    database = server_settings.get('database', 0)
    return redis.Redis(host=host, port=port, db=database)

@task(name='megaphone.send_announcement')
def send_announcement(announcement_id):
    Announcement = get_model('megaphone','Announcement')
    announcement = Announcement.objects.get(pk=announcement_id)

    channels = []
    for site in announcement.sites.all():
        channels.append('megaphone' + str(site.id))
        cache.set(str(site.id) + 'Megaphone', announcement, 60 * 60)

    msg = {'channels': channels, 'data': [announcement.main_text, announcement.pub_date]}
    server = _get_juggernaut_server()
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    server.publish('juggernaut', json.dumps(msg, default=dthandler))
