from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'godjango.views.home', name='home'),
    # url(r'^godjango/', include('godjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^about/$', 'home.views.about'),
    url(r'^feedback/$', 'home.views.feedback'),
    url(r'^(?P<video_id>\d+)-(?P<slug>[-\w]+)/$', 'home.views.video')
)
