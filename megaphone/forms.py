from django import forms
from megaphone.models import Announcement

class AnnouncementForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        exclude = ('celery_task_id',)

class SiteAnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        exclude = ('celery_task_id', 'sites')

class NowAnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        exclude = ('celery_task_id', 'sites', 'pub_date')

class ShowAnnouncementForm(forms.ModelForm):

	class Meta:
		model = Announcement
		exclude = ('celery_task_id')
