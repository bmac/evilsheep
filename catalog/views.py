# Create your views here.
from catalog.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def show_product(request, supercat_slug, subcat_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, category__slug=subcat_slug, category__super_category__slug=supercat_slug)
    meta_keywords = product.meta_keywords
    meta_description = product.meta_description
    return render_to_response('catalog/view_product.html', locals(), context_instance=RequestContext(request))


def index(request):
    featured_offers = Product.active.filter(is_featured=True)
    return render_to_response('catalog/index.html', locals(), context_instance=RequestContext(request))

def show_super_cat(request, supercat_slug):
    super_cat = SuperCategory.active.get(slug=supercat_slug)
    sub_categoies = SubCategory.active.filter(super_category=super_cat)
    meta_keywords = super_cat.meta_keywords
    meta_description = super_cat.meta_description
    return render_to_response('catalog/super_cat.html', locals(), context_instance=RequestContext(request))


def show_sub_cat(request, supercat_slug, subcat_slug):
    current_cat = SuperCategory.active.get(slug=cat_slug)
    sub_categoies = SubCategory.active.filter(super_category=super_cat)
    meta_keywords = current_cat.meta_keywords
    meta_description = current_cat.meta_description
    return render_to_response('catalog/sub_cat.html', locals(), context_instance=RequestContext(request))







