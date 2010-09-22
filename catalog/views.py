# Create your views here.
from catalog.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from evilsheep.cart import cart
from catalog.forms import AddProductToCartForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def show_product(request, supercat_slug, subcat_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, category__slug=subcat_slug, category__super_category__slug=supercat_slug, is_active=True)
    meta_keywords = product.meta_keywords
    meta_description = product.meta_description
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = AddProductToCartForm(request, postdata)
        if form.is_valid():
            cart.add_to_cart(request)
            #remove the test cookie
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        form = AddProductToCartForm(request)
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    #set a test cookie with the get request
    request.session.set_test_cookie()
    return render_to_response('catalog/view_product.html', locals(), context_instance=RequestContext(request))


def index(request):
    featured_offers = Product.active.filter(is_featured=True)
    return render_to_response('catalog/index.html', locals(), context_instance=RequestContext(request))

def show_super_cat(request, supercat_slug):
    super_cat = get_object_or_404(SuperCategory, slug=supercat_slug, is_active=True)
    sub_categories = SubCategory.active.filter(super_category=super_cat)
    meta_keywords = super_cat.meta_keywords
    meta_description = super_cat.meta_description
    return render_to_response('catalog/super_cat.html', locals(), context_instance=RequestContext(request))


def show_sub_cat(request, supercat_slug, subcat_slug):

    current_cat = get_object_or_404(SubCategory, slug=subcat_slug, 
                   super_category__slug=supercat_slugm, is_active=True)
    products = Product.active.filter(category__slug=subcat_slug).order_by('name')
    paginator = Paginator(products, 16) # Show 8 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    current_cat = get_object_or_404(SubCategory, slug=subcat_slug, super_category__slug=supercat_slug, is_active=True)
    sub_categories = SubCategory.active.filter(super_category__slug=supercat_slug)
    meta_keywords = current_cat.meta_keywords
    meta_description = current_cat.meta_description
    
    return render_to_response('catalog/sub_cat.html', locals(), context_instance=RequestContext(request))







