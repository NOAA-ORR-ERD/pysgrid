from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wms.views.fvDo'),
    url(r'^doc', 'wms.views.documentation'),
    url(r'^wms/(?P<dataset>.*)/', 'wms.views.wms'),
    url(r'^wmstest/$', 'wms.views.wmstest'),
    url(r'^wmstest/openlayers/(?P<filepath>.*)', 'wms.views.openlayers'),
    url(r'^crossdomain.xml', 'wms.views.crossdomain'),
    #url(r'^testdb', 'wms.views.testdb'),
    url(r'^index', 'wms.views.index'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
    


