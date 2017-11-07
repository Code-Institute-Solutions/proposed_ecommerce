from django.shortcuts import render
from .models import Product


def products_list(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, "products.html",
                  {"products": products, "query": query})
