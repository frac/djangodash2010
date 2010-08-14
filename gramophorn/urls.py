from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Example:
    # (r'^gramophorn/', include('gramophorn.foo.urls')),
    (r'^settings/', include('gramophorn.conf.urls')),
    (r'^$', direct_to_template, {'template': "index.html"} ),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
