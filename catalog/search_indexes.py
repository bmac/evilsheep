import datetime
from haystack.indexes import *
from haystack import site
from evilsheep.catalog.models import Product

class ProductIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='name')


site.register(Product, ProductIndex)

