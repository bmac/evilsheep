from evilsheep.catalog.models import Movie, SubCategory
from evilsheep.utils.utils import slugify
from django.core.files import File
import xml.dom.minidom
import urllib
import os



def get_a_document(name="/tmp/doc.xml"):
    return xml.dom.minidom.parse(name)

dom = get_a_document(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'products/dvdg4g.xml'))

mov_cat = SubCategory.objects.all()[0]





for node in dom.getElementsByTagName('item'):
    m = Movie()
    title = node.getElementsByTagName('title')[0].firstChild.nodeValue
    title_junk_chars = title.find('(')
    if title_junk_chars is not -1:
        title_junk_chars += -1
        m.name = title[:title_junk_chars]
    else:
        m.name = title

    title_junk_chars = m.name.find('DVD')
    if title_junk_chars is not -1:
        title_junk_chars += -1
        m.name = m.name[:title_junk_chars]

        
    print 'name ', m.name
    m.slug = slugify(m.name)
    print 'slug ', m.slug
    
    m.price = '20.00'
    m.description = node.getElementsByTagName('description')[0].firstChild.nodeValue
    m.brand = node.getElementsByTagName('brand_name')[0].firstChild.nodeValue


    m.category = mov_cat

    m.meta_keywords = ''
    m.meta_description = ''


    m.quantity = node.getElementsByTagName('qty_avail')[0].firstChild.nodeValue
    m.sku = node.getElementsByTagName('product_sku')[0].firstChild.nodeValue
    m.doba_id = node.getElementsByTagName('item_id')[0].firstChild.nodeValue
    m.doba_price = node.getElementsByTagName('price')[0].firstChild.nodeValue
    m.doba_shipping_cost = node.getElementsByTagName('ship_cost')[0].firstChild.nodeValue


    
    url = node.getElementsByTagName('image_file')[0].firstChild.nodeValue
    result = urllib.urlretrieve(url) # image_url is a URL to an image


    m.thumbnail.save(
        os.path.basename(url),
        File(open(result[0]))
    )
    
    m.image.save(
        os.path.basename(url),
        File(open(result[0]))
    )

    m.save()
    print m


    
    
 

    
