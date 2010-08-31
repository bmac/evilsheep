from django.db import models
from catalog.models import Product
# Create your models here.


class CartItem(models.Model):
    cart_id  = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('catalog.product', unique=False)
    
    class Meta:
        ordering = ['date_added']
        

    def total(self):
        return self.quantity * self.product 
    
    def name(self):
        return self.product.name
    
    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()
    
    def augement_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    def __unicode__(self):
        return '%d %s in cart %s' % (quantity, product, cart_id) 
