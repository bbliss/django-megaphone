import datetime
from django.utils import timezone
from django.shortcuts import render
from django.contrib.sites.models import Site, get_current_site

from megaphone.models import Announcement
from megaphone.forms import AnnouncementForm, SiteAnnouncementForm
from megaphone.forms import NowAnnouncementForm

def announcement_list(request):
    site = get_current_site(request)
    announcements = Announcement.objects.filter(sites=site, pub_date__lte=timezone.now())

    return render(request, 'megaphone/announcement_list.html', {
        'announcements': announcements,
        'site_id': site.id
    })

def announce(request):
    site = get_current_site(request)
    
    if request.method == "POST":
        a_form = AnnouncementForm(request.POST)
        if a_form.is_valid():
            new_announcement = a_form.save()
    else:
        a_form = AnnouncementForm()
    
    return render(request, 'megaphone/announce.html', {
        'a_form': a_form,
    })

def site_announce(request):
    site = get_current_site(request)
    
    if request.method == "POST":
        a_form = SiteAnnouncementForm(request.POST)
        if a_form.is_valid():
            a_form.cleaned_data['sites'] = [site.id]
            new_announcement = a_form.save()
    else:
        a_form = SiteAnnouncementForm()
    
    return render(request, 'megaphone/announce.html', {
        'a_form': a_form,
    })

def now_announce(request):
    site = get_current_site(request)

    if request.method == "POST":
        a_form = NowAnnouncementForm(request.POST)
        if a_form.is_valid():
            a_form.cleaned_data['sites'] = [site.id]
            a_form.cleaned_data['pub_date'] = timezone.now()
            new_announcement = a_form.save()
        else:
            print "derp happened.", a_form.errors
    else:
        a_form = NowAnnouncementForm()

    return render(request, 'megaphone/announce.html', {
        'a_form': a_form,
    })
