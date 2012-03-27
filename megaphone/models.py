from django.db import models
from django.contrib.sites.models import Site
from django.utils import timezone

from django.conf import settings
try:
    CHANNEL_NAME = settings.MEGAPHONE_CHANNEL
except:
    CHANNEL_NAME = 'megaphone'

import datetime
import redis
import json

from megaphone.tasks import delayed_announcement

class Announcement(models.Model):
    main_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    sites = models.ManyToManyField(Site)

    def __unicode__(self):
        return "Announcement: " + self.main_text[:80]
    def save(self):
        super(Announcement, self).save()

        # Once the announcement has been saved, either send it to Redis
        # immediately, or schedule a task to send it on the pub date.
        if self.pub_date <= timezone.now():
            channels = []
            for site in self.sites.all():
                channels.append(site)
            
            msg = {'channels': ['megaphone'], 'data': [self.main_text, self.pub_date] }
            server = redis.Redis()
            dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
            server.publish('juggernaut', json.dumps(msg, default=dthandler))
        else:
            msg = {'channels': ['megaphone'], 'data': [self.main_text, self.pub_date] }
            delayed_announcement.apply_async(args=[msg], eta=self.pub_date)
