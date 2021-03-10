from django.shortcuts import render
from .models import Product

# Create your views here.

def shop(request):
    products=Product.objects.all()
    return render(request, "shop_template/shop.html", {"products":products})

