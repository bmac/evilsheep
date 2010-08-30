from django.contrib import admin
from evilsheep.catelog.models import Product, SuperCategory, SubCategory, Book

class BookAdmin(admin.ModelAdmin):
    pass

class SuperCategoryAdmin(admin.ModelAdmin):
    pass

class SubCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(SuperCategory, SuperCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)


