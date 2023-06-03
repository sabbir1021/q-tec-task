from django.shortcuts import render, get_object_or_404
from django.views import View 
from .models import GenericFilter,ProductFilter, Product,  Category
from django.views.generic import ListView

# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = "shop/home.html"


class CategoryProductView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        products = Product.objects.filter(category__id = pk)
        product_filter = GenericFilter.objects.all()
        min_price = min(products.values_list('price'))[0]
        max_price = max(products.values_list('price'))[0]
        context = {
            'category': category,
            'products':products,
            'count': products.count(),
            'min_price': min_price,
            'max_price': max_price,
            'product_filter' : product_filter
        }
        return render(request, "shop/category_products.html", context)
   


def load_search_and_filter(request):
    price_range = request.GET.getlist('price_range[]')
    filter_value_list = request.GET.getlist('filter_value_list[]')
    category_id = request.GET.getlist('category_id')[0]
    category = get_object_or_404(Category, id=category_id)
    if filter_value_list:
        products = Product.objects.filter(category__id = category_id, price__range=(price_range[0],price_range[1]), productfilter__value__id__in = filter_value_list).distinct()
    elif price_range:
        products = Product.objects.filter(category__id = category_id, price__range=(price_range[0],price_range[1]))
    else:
        products = Product.objects.filter(category__id = category_id)
    return render(request, 'partials/filter.html', {'products':products, 'category': category, 'count': products.count()})

