"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from pages.views import home_view, contact_view, get_session
from accounts.views import auth_view, login, signup, logout, cart_view
from products.views import products_view, product_details
from orders.views import checkout, payment, thanks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('products/', products_view),
    path('auth/', auth_view),
    path('contact/', contact_view),
    re_path(r'^auth/signup.', signup),
    re_path(r'^auth/login.', login),
    path('logout/', logout),
    re_path(r'^product/[0-9]', product_details),
    re_path(r'^cart/', cart_view),
    re_path(r'^checkout/', checkout),
    re_path(r'^payment/', payment),
    re_path(r'^thank-you-page/', thanks),
   ]
