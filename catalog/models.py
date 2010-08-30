from django.db import models
from settings import MEDIA_ROOT
# Create your models here.

class ProductActiveManager(models.Manager):
    def get_query_set(self):
        return super(ProductActiveManager, self).get_query_set().filter(is_active=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for this product URL, created from name.')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey('catalog.SubCategory')


    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    bonus_offer = models.ForeignKey('catalog.SuperCategory', blank=True, null=True)

    image = models.ImageField(upload_to=MEDIA_ROOT)
    thumbnails = models.ImageField(upload_to=MEDIA_ROOT)
    
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag.')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag.')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #supplier data
    quantity = models.IntegerField(default=0)
    sku = models.CharField(max_length=100)
    
    doba_id = models.CharField(blank=True, max_length=100)
    doba_price = models.DecimalField(max_digits=9, decimal_places=2)
    doba_shipping_cost = models.DecimalField(max_digits=9, decimal_places=2)
   

    # managers 
    objects = models.Manager() # The default manager.
    active = ProductActiveManager() # The active products manager.


    class Meta:
        ordering = ['-created_at']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('products_product', (), {'product_slug': self.slug })

class CatActiveManager(models.Manager):
    def get_query_set(self):
        return super(ProductActiveManager, self).get_query_set().filter(is_active=True)

class SuperCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag.')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag.')

    # managers 
    objects = models.Manager() # The default manager.
    active = CatActiveManager() # The active products manager.

    class Meta:
        ordering = ['name']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catelog_supercategory', (), {'supercat_slug': self.slug })


class SubCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    super_category = models.ForeignKey(SuperCategory)
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag.')
    meta_description = models.CharField(max_length=255, help_text='Content for description meta tag.')
    

    product_queue = models.ForeignKey(Product)


    # managers 
    objects = models.Manager() # The default manager.
    active = CatActiveManager() # The active products manager.

    class Meta:
        ordering = ['name']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catelog_subcategory', (), {'subcat_slug': self.slug })



class Book(Product):
    author = models.CharField(max_length=255)
    binding = models.CharField(blank=True, null=True, max_length=255)
    edition = models.CharField(blank=True, null=True, max_length=255)
    language = models.CharField(blank=True, null=True, max_length=100)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(blank=True, null=True, max_length=255)
    subject = models.CharField(blank=True, null=True, max_length=255)
    
    
        
        
        
