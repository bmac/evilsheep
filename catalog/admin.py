from django.contrib import admin
from evilsheep.catalog.models import Product, SuperCategory, SubCategory, Book

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
                'fields': ('name', 'slug', 'author', 'price', 'description', 'category', 'is_active', 'is_featured', 'image', 'thumbnail', 'meta_keywords', 'meta_description', )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('brand', 'bonus_offer', 'quantity', 'sku', 'doba_id', 'doba_price', 'doba_shipping_cost', 'binding', 'edition', 'language', 'pages', 'publisher', 'subject',)
        }),
    )
    

class SuperCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)


