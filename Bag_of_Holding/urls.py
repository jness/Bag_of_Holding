from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hub.views.home', name='home'),
    url(r'^profile/$', 'hub.views.profile', name='profile'),
    url(r'^login/$', 'hub.views.mylogin', name='mylogin'),
    url(r'^logout/$', 'hub.views.mylogout', name='mylogout'),
    url(r'^character/(?P<character_id>[0-9]+)/$', 'hub.views.character', name='character'),
    url(r'^add/(?P<character_id>[0-9]+)/$', 'hub.views.add', name='add'),
    url(r'^add_character/$', 'hub.views.add_character', name='add_character'),
    url(r'^update/(?P<character_id>[0-9]+)/(?P<item_id>[0-9]+)/$', 'hub.views.update', name='update'),
    url(r'^trash/(?P<character_id>[0-9]+)/(?P<item_id>[0-9]+)/$', 'hub.views.trash', name='trash'),
    url(r'^admin/', include(admin.site.urls)),
)
