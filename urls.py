from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'wager.views.index', name='home'),
    url(r'^(?P<slug>[a-z0-9\-_]+)/$', 'wager.views.wager', name='wager'),
)
