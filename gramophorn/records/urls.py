from django.conf.urls.defaults import *
from gramophorn.records import views as resource

urlpatterns = patterns('',                                                                                                                                  
    (r'^$', resource.list),
    (r'^(?P<model>[-\w]+)/new/$',resource.new),
    (r'^disk/new/(?P<album_id>\d+)/$',resource.new_disk),
    (r'^tracks/new/(?P<disk_id>\d+)/$',resource.new_tracks),
    #(r'^add/(?P<model>[-\w]+)/$',resource.add),
    #(r'^wave/(?P<slug>[-\w]+)$',object_detail,detail_wave),
    #(r'^wave/(?P<object_id>\d+)$',object_detail,detail_wave),
)  

