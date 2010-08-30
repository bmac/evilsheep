from django.contrib import admin
from evilsheep.cart.models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(CartItem, CartItemAdmin)


