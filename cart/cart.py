from evilsheep.cart.models import CartItem 

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _gen_secret_key()
    return request.session[CART_ID_SESSION_KEY]]


def _gen_secret_key():
    cart_id = ''
    chars = 'ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range (cart_id_length):
        cart_id += chars[random.randint(0, len(chars)-1)]
    return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    postdata = request.POST.copy()

    product_slug = postdata.get('product_slug', '')
    quantity = postdata.get('quantity', 1)
    
    p = get_object_or_404(Product, slug=product_slug)
    
    cart_products = get_cart_items(request)
    
    product_in_cart = False
    #check to see if the product is already in the cart
    for cart_item in cart_products:
        if cart_item.product.id == p.id:
            cart_item.augement_quantity(quantity)
            product_in_cart = True
        
    if not product_in_cart:
        # create item and save it
        ci = CartItem()
        ci.product = p
        ci.cart_id = _cart_id(request)
        ci.quantity = quantity
        ci.save()

def cart_distinct_item_count(request):
    return get_cart_items(request).count()

