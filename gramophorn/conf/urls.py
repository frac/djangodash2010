from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from gramophorn.conf import views as resource

urlpatterns = patterns('',                                                                                                                                  
    (r'^$', direct_to_template, {'template': "conf/index.html"} ),
    (r'^install/', resource.install),
)  

