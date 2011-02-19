from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^$', 'wager.views.index', name='home'),
    url(r'^/(?P<slug>[a-z0-9\-_]+)/$', 'wager.views.wager', name='wager'),
)
