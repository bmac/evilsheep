from evilsheep import settings
from evilsheep.cart import cart
from catalog.models import SubCategory

def ecomstore(request):
    item_count = cart.cart_distinct_item_count(request)
    sub_cats = SubCategory.active.all()
    return {
        'site_name' : settings.SITE_NAME,
        'meta_keywords' : settings.META_KEYWORDS,
        'meta_description' : settings.META_DESCRIPTION,
        'item_count' : item_count,
        'sub_cats' : sub_cats,
        }
