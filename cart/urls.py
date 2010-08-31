from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('evilsheep.cart.views',
                       (r'^$', 'show_cart', {}, 'show_cart'),
                       
)
