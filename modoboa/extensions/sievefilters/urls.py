from django.conf.urls import patterns

urlpatterns = patterns('modoboa.extensions.sievefilters.views',
    (r'^$', 'index'),
    (r'^savefs/(?P<name>.+)/$', 'savefs'),
    (r'^newfs/$', 'new_filters_set'),
    (r'^removefs/(?P<name>.+)/$', 'remove_filters_set'),
    (r'^activatefs/(?P<name>.+)/$', 'activate_filters_set'),
    (r'^downloadfs/(?P<name>.+)/$', 'download_filters_set'),
    (r'^templates/(?P<ftype>\w+)/$', 'get_templates'),
    (r'^(?P<setname>.+)/newfilter/$', 'newfilter'),
    (r'^(?P<setname>.+)/editfilter/(?P<fname>.+)/$', 'editfilter'),
    (r'^(?P<setname>.+)/removefilter/(?P<fname>.+)/$', 'removefilter'),
    (r'^(?P<setname>.+)/togglestate/(?P<fname>.+)/$', 
     'toggle_filter_state'),
    (r'^(?P<setname>.+)/moveup/(?P<fname>.+)/$', 
     'move_filter_up'),
    (r'^(?P<setname>.+)/movedown/(?P<fname>.+)/$', 
     'move_filter_down'),
    (r'^(?P<name>.+)/$', 'getfs'),
)
