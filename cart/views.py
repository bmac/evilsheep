# Create your views here.
from evilsheep.cart import cart
from django.shortcuts import render_to_response
from django.template import RequestContext


def show_cart(request):
    page_title = 'Shopping Cart'
    cart_item_count = cart.cart_distinct_item_count(request)
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    return render_to_response('cart/cart.html', locals(), context_instance=RequestContext(request))
