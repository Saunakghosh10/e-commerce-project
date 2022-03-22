from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from pages.views import navbar_context, get_session
from .models import Product
import re
from accounts.models import User, Cart
from django.core import serializers

# Create your views here.
def products_view(request):
    get_session(request)

    selected = 0
    page_no = 1
    max_ = 13 * page_no
    min_ = max_ - 13
    all_products = Product.objects.all()
    page_products = all_products.order_by("id")

    if request.method == 'POST':
        if request.POST.get('page-no'):
            page_no = int(request.POST.get('page-no'))
            max_ = 13 * page_no
            min_ = max_ - 12 - page_no 

        sort = request.POST.get('sort')
        if sort == 'default':
            page_products = all_products.order_by("id")
            selected = 0
        elif sort == 'price':
            page_products = all_products.order_by("price")
            selected = 1
        elif sort == '!price':
            page_products = all_products.order_by("-price")
            selected = 2
        elif sort == 'alpha':
            page_products = all_products.order_by("name")
            selected = 3
        elif sort == '!alpha':
            page_products = all_products.order_by("-name")
            selected = 4
    
    page_products = page_products[min_:max_]

    context = {"page_no":page_no, "select":selected}
    for i, model in enumerate(page_products):
        context["p" + str(i + 1)] = model

    context.update(navbar_context)
    
    return render(request, "products.html", context)

def product_details(request):
    get_session(request)

    no_of_prod = len(Product.objects.all())
    full_path = str(request.get_full_path())
    pid = int(re.search('[0-9]+$', full_path).group(0))
    print(pid)

    products = list(Product.objects.all()[pid-1:pid+4])
    if (pid+4 > no_of_prod):
        excess = pid+4 - no_of_prod
        products += list(Product.objects.all()[0:excess+1])
    
    context = {}
    
    for i, model in enumerate(products):
        context["p" + str(i + 1)] = model
    
    context.update(navbar_context)

    if request.method == "POST" and 'user' in list(request.session.keys()):
        user_email = dict(request.session.items())['user']
        user_obj = User.objects.filter(email=user_email)[0]
        quantity = int(request.POST.get('quantity'))
        
        if not hasattr(user_obj, 'cart'):
            Cart.objects.create(user=user_obj)

        user_cart = Cart.objects.filter(user=user_obj)[0]
        
        if quantity > 1:
            for i in range(quantity):
                user_cart.cart += f"{str(pid)} "
        else:
            user_cart.cart += f"{str(pid)} "
        user_cart.save()

    return render(request, "productdetails.html", context)