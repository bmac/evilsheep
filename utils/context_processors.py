from evilsheep import settings
from evilsheep.cart import cart


def ecomstore(request):
    item_count = cart.cart_distinct_item_count(request)
    
    return {
        'site_name' : settings.SITE_NAME,
        'meta_keywords' : settings.META_KEYWORDS,
        'meta_description' : settings.META_DESCRIPTION,
        'item_count' : item_count,
        }
