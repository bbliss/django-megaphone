import datetime
import redis
import json

from django.db import models
from django.contrib.sites.models import Site
from django.utils import timezone
from django.conf import settings

from celery.task.control import revoke
from megaphone.tasks import send_announcement

class Announcement(models.Model):
    main_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    sites = models.ManyToManyField(Site)
    celery_task_id = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "Announcement: " + self.main_text[:80]
    def save(self):
        super(Announcement, self).save()

        # If the announcement is to be published immediately, be sure to delay it at least a few seconds
        # so that we can ensure the m2m on site has been saved and channels can be derived.
        print "pub date:", self.pub_date
        print "tznow:", timezone.now()
        print "future:", self.pub_date > timezone.now()
        if self.pub_date <= timezone.now():
            #celery_eta = timezone.now() + datetime.timedelta(seconds=5)
            celery_eta = datetime.datetime.now(tz=timezone.get_default_timezone())
            print "set eta to now plus 5 secs.", celery_eta
        else:
            celery_eta = self.pub_date
            print "set eta to pub date.", celery_eta

        self.celery_task_id = send_announcement.apply_async(args=[self.id], eta=celery_eta)
        
        super(Announcement, self).save()
    def delete(self):
        super(Announcement, self).delete()
        revoke(self.celery_task_id)
