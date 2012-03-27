import datetime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.sites.models import Site, get_current_site

from megaphone.models import Announcement
from megaphone.forms import AnnouncementForm

def announcement_list(request):
    site = get_current_site(request)
    announcements = Announcement.objects.filter(sites=site, pub_date__lte=timezone.now())

    return render(request, 'megaphone/announcement_list.html', {
        'announcements': announcements,
    })

def announce(request):
    site = get_current_site(request)
    
    if request.method == "POST":
        a_form = AnnouncementForm(request.POST)
        if a_form.is_valid():
            new_announcement = a_form.save()
    else:
        a_form = AnnouncementForm()
    
    print "a_form:", a_form

    return render(request, 'megaphone/announce.html', {
        'a_form': a_form,
    })

