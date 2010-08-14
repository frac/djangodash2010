from django.conf.urls.defaults import *
from gramophorn.records import views as resource

urlpatterns = patterns('',                                                                                                                                  
    (r'^$', resource.list),
    #(r'^wave/(?P<slug>[-\w]+)$',object_detail,detail_wave),
    #(r'^wave/(?P<object_id>\d+)$',object_detail,detail_wave),
)  

