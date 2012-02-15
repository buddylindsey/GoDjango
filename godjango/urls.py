from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from home.rss import LatestVideos

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin Stuffs
    url(r'^admin/', include(admin.site.urls)),

    # User auth stuffs
    url(r'', include('social_auth.urls')),
    url(r'^dashboard/$', 'users.views.dashboard', name="dashboard"),
    url(r'^login/$', redirect_to, { 'url': '/login/github' }),
    url(r'^logout/$', 'users.views.logout'),

    # home
    url(r'^$', 'home.views.index', name="index"),
    url(r'^about/$', 'home.views.about', name="about"),
    url(r'^feedback/$', 'contact.views.feedback', name="feedback"),
    url(r'^rss/main', LatestVideos()),
    url(r'^(?P<video_id>\d+)-(?P<slug>[-\w]+)/$', 'home.views.video')
)
