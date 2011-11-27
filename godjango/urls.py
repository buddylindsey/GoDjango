from django.conf.urls.defaults import patterns, include, url
from home.rss import LatestVideos

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^about/$', 'home.views.about'),
    url(r'^feedback/$', 'home.views.feedback'),
    url(r'^rss/main', LatestVideos()),
    url(r'^(?P<video_id>\d+)-(?P<slug>[-\w]+)/$', 'home.views.video')
)
