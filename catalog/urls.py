from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('evilsheep.catalog.views',
                       (r'^$', 'index', {}, 'catalog_home'),
                       (r'^(?P<supercat_slug>[-\w]+)/(?P<subcat_slug>[-\w]+)/$', 'show_sub_cat', {}, 'catalog_subcategory'),
                       (r'^(?P<supercat_slug>[-\w]+)/$', 'show_super_cat', {}, 'catalog_supercategory'),
                       url(r'^(?P<supercat_slug>[-\w]+)/(?P<subcat_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', 'show_product', name='catalog_product'),

)
