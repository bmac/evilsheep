import Image
from evilsheep.catalog.models import Product

height = 200
width = 150


for p in Product.objects.all():
    thumb = Image.open(p.thumbnail.path)
    thumb.resize((width, height), Image.ANTIALIAS)
    thumb.save(p.thumbnail.path)


