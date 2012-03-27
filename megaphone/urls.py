from django.conf.urls.defaults import *

urlpatterns = patterns('megaphone.views',
    url(r'^$',
        'announcement_list',
        name='megaphone_announcement_list',
    ),
    url(r'^announce/$',
        'announce',
        name='megaphone_announce',
    ),
)
