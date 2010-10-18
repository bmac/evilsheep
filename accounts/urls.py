from django.conf.urls.defaults import *

urlpatterns = patterns('evilsheep.accounts.views',
                       (r'^(?P<username>[-\w]+)/$', 'show_user', {}, 'show_user'),
                       
)
