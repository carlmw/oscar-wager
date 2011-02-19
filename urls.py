from django.conf.urls.defaults import *
from django.conf import settings
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^$', 'wager.views.index', name='home'),
    url(r'^(?P<slug>[a-z0-9\-_]+)/$', 'wager.views.wager', name='wager'),
    url(r'^(?P<slug>[a-z0-9\-_]+)/pick/$', 'wager.views.pick', name='pick'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)