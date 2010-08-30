# Create your views here.


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    meta_keyword = product.meta_keyword
    meta_description = product.meta_description
    return render_to_response('catalog/view_product.html', locals(), context_instance=RequestContext(request))


def index(request):
    featured_offers = Product.active.filter(is_featured=True)
    return render_to_response('catalog/index.html', locals(), context_instance=RequestContext(request))

def show_super_cat(request, supercat_slug):
    super_cat = SuperCategory.active.get(slug=supercat_slug)
    sub_categoies = SubCategory.active.filter(super_category=super_cat)
    meta_keyword = super_cat.meta_keyword
    meta_description = super_cat.meta_description
    return render_to_response('catalog/super_cat.html', locals(), context_instance=RequestContext(request))


def show_sub_cat(request, supercat_slug, subcat_slug):
    current_cat = SuperCategory.active.get(slug=cat_slug)
    sub_categoies = SubCategory.active.filter(super_category=super_cat)
    meta_keyword = current_cat.meta_keyword
    meta_description = current_cat.meta_description
    return render_to_response('catalog/sub_cat.html', locals(), context_instance=RequestContext(request))







