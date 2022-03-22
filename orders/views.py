from django.shortcuts import render
from accounts.models import User, Cart
from .models import Order
import datetime
import pytz

# Create your views here.
def checkout(request):
    context = {}

    if request.method == 'POST':
        order_total = float(request.POST.get('sbmt-btn'))
        disc_per = 10
        discount = round((disc_per / 100) * order_total, 2)
        tax_per = 4
        tax = round((tax_per / 100) * (order_total - discount), 2)
        ship_fee = 5.43
        total = round(order_total - discount + tax + ship_fee, 2)
    
        context = {"order_total":order_total, "disc":discount, "tax":tax, "ship":ship_fee, "total":total, "per":[disc_per, tax_per]}
    
    return render(request, 'checkout.html', context)

def payment(request):

    context = {}
    if request.method == 'POST':
        total = float(request.POST.get('btn'))
        context['total'] = total
        context['address'] = request.POST.get('address')

    return render(request, 'payment.html', context)

def thanks(request):
    context={}
   
    if request.method == 'POST' and 'user' in request.session.keys():
        user_email = dict(request.session.items())['user']
        user_obj = User.objects.filter(email=user_email)[0]
        products = Cart.objects.filter(user=user_obj)[0].cart.split()
        price = float(request.POST.get('button-price'))
        address = request.POST.get('address-holder')

        order = Order.objects.create(user=user_obj, products=products, price=price, address=address, datetime=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')))
        order.save()

    return render(request, 'thanks.html', context)