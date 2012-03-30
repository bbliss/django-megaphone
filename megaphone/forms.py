from django import forms
from megaphone.models import Announcement

class AnnouncementForm(forms.ModelForm):
    
    class Meta:
        model = Announcement
        exclude = ('celery_task_id',)
