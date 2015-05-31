from django.conf.urls import patterns, include, url
from django.contrib import admin
from meetups import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'meetups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^meetups$', views.MeetupList.as_view(), name='meetup-list'),
    url(r'^meetups/(?P<pk>[0-9]+)$', views.MeetupDetail.as_view(), name='meetup-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
