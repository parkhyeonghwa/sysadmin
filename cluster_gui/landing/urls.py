__author__ = 'sype'

from django.conf.urls.defaults import patterns, include, url



urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'landing.views.monitor_cluster', name='monitor_cluster'),


    # url(r'^cluster_gui/', include('cluster_gui.foo.urls')),
    #url(r'^cluster_gui/', include(landing.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:


    # Uncomment the next line to enable the admin:

)

