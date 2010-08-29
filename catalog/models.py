from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.Slugield(max_length=255, unique=True, help_text='Unique value for this product URL, created from name.')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey('category.SubCategory')


    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    bonus_offer = models.ForeignKey('category.SuperCategory', blank=True, null=True)

    image = models.ImageField()
    thumbnails = models.ImageField()
    
    meta_keywords = models.Charfield(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag.')
    meta_description = models.Charfield(max_length=255, help_text='Content for description meta tag.')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #supplier data
    quantity = models.IntegerField(default=0)
    sku = models.CharField(max_length=100)
    
    doba_id = models.CharField(blank=True, max_length=100)
    doba_price = models.DecimalField(max_digits=9, decimal_places=2)
    doba_shipping_cost = models.DecimalField(max_digits=9, decimal_places=2)
    

    class Meta:
        ordering = ['-created_at']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('products_product', (), {'product_slug': self.slug })


class SuperCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catelog_supercategory', (), {'supercat_slug': self.slug })


class SubCategory(model.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    supercat = models.ForeignKey(SuperCategory)
    
    product_queue = models.ForeignKey(Product)

    class Meta:
        ordering = ['name']
        

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catelog_subcategory', (), {'subcat_slug': self.slug })



class Book(Product):
    author = models.CharField(max_length=255)
    binding = models.CharField(blank=True, max_length=255)
    edition = models.CharField(blank=True, max_length=255)
    language = models.CharField(blank=True, max_length=100)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(blank=True, max_length=255)
    subject = models.CharField(blank=True, max_length=255)
    
    
        
        
        
