import re
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pages.views import navbar_context, home_view, get_session
from products.models import Product
from itertools import groupby

# Create your views here.
from .models import User, Cart


def auth_view(request):
    get_session(request)
    
    return render(request, 'reg.html', navbar_context)


def signup(request):
    get_session(request)
    
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pass')

        if User.objects.filter(email=email).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            obj = User.objects.create(email=email, password=pwd)
            obj.save()
            return redirect(auth_view)
    else:
        return render(request, 'reg.html', navbar_context)


def login(request):
    get_session(request)
    
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pass')

        check_user = User.objects.filter(email=email, password=pwd)
        
        if check_user:
            request.session['user'] = email
            if request.POST.get('name'):
                name = request.POST.get('name')
                navbar_context["uname"] = name.split()[0]
            else:
                navbar_context["uname"] = email
            return redirect(home_view)
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'reg.html')

def logout(request):
    get_session(request)
    
    try:
        del request.session['user']
    except:
        return redirect(auth_view)
    
    navbar_context["uname"] = ""
    
    return redirect(auth_view)


def cart_view(request):
    get_session(request)


    context = {}
    qset = Product.objects.none()

    if 'user' in list(request.session.keys()):
        user_email = dict(request.session.items())['user']
        user_obj = User.objects.filter(email=user_email)[0]

        if not hasattr(user_obj, 'cart'):
            Cart.objects.create(user=user_obj)
        
        cart = Cart.objects.filter(user=user_obj)[0].cart.split()

        if request.method == 'POST' and request.POST.get("delete"):
            cart.remove(request.POST.get("delete"))
            user_obj.cart.cart = ' '.join(cart) + " "
            user_obj.cart.save()

        quantity = {}
        total = 0.00

        for i, pid in enumerate(cart):
            #print(i, pid)
            if pid in quantity.keys():
                quantity[pid] += 1
            else:
                quantity[pid] = 1

            qset |= Product.objects.filter(id=int(pid))
            total += float(str(Product.objects.filter(id=int(pid))[0].price))


    context = {"qset":qset,"quantity":list(quantity.values()),"total":total, "qtotal":len(cart)}

    context.update(navbar_context)

    return render(request, 'cart.html', context)