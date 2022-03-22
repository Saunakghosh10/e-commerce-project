from django.contrib import admin

from products.models import Product

class MyModelAdmin(admin.ModelAdmin):
    readonly_fields=('cart',)

# Register your models here.
admin.site.register(Product)