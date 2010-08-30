from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('evilsheep.catalog.views',
                       (r'^$', 'index', {}, 'catalog_home'),
                       (r'^(?P<supercat_slug>[-\W]+)/(?P<subcat_slug>[-\W]+)/$', 'show_sub_cat', {}, 'catalog_subcategory'),
                       (r'^(?P<supercat_slug>[-\W]+)/$', 'show_sub_cat', {}, 'catalog_subcategory'),
                       (r'^product/(?P<product_slug>[-\W]+)/$', 'show_product', {}, 'catalog_product'),
)
