from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hub.views.home', name='home'),
    url(r'^login/$', 'hub.views.mylogin', name='mylogin'),
    url(r'^logout/$', 'hub.views.mylogout', name='mylogout'),

    url(r'^profile/$', 'hub.views.profile', name='profile'),
    url(r'^profile/update_password/$', 'hub.views.update_password', name='update_password'),
    url(r'^profile/create_character/$', 'hub.views.create_character', name='create_character'),

    url(r'^character/(?P<character_id>[0-9]+)/$', 'hub.views.character', name='character'),
    url(r'^character/(?P<character_id>[0-9]+)/new/$', 'hub.views.create_item', name='create_item'),
    url(r'^character/(?P<character_id>[0-9]+)/rename_slot/(?P<slot_id>[0-9]+)/$', 'hub.views.rename_slot', name='rename_slot'),
    url(r'^character/(?P<character_id>[0-9]+)/delete_slot/(?P<slot_id>[0-9]+)/$', 'hub.views.delete_slot', name='delete_slot'),
    url(r'^character/(?P<character_id>[0-9]+)/create_slot/$', 'hub.views.create_slot', name='create_slot'),
    url(r'^character/(?P<character_id>[0-9]+)/update/(?P<item_id>[0-9]+)/$', 'hub.views.update_item', name='update_item'),

    url(r'^add/(?P<character_id>[0-9]+)/$', 'hub.views.add', name='add'),
    url(r'^update/(?P<character_id>[0-9]+)/(?P<item_id>[0-9]+)/$', 'hub.views.update', name='update'),
    url(r'^trash/(?P<character_id>[0-9]+)/(?P<item_id>[0-9]+)/$', 'hub.views.trash', name='trash'),
    url(r'^admin/', include(admin.site.urls)),
)
