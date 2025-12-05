from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Product
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def indexFur(request):
    return render(request, 'furniture/index.html')

def aboutFur(request):
    return render(request, 'furniture/about.html')

def blogDetial(request):
    return render(request, 'furniture/blog_detail.html')

def blog(request):
    return render(request, 'furniture/blog.html')

def cart(request):
    return render(request, 'furniture/cart.html')

def checkOut(request):
    return render(request, 'furniture/checkout.html')

def contact(request):
    return render(request, 'furniture/contact.html')

def detail(request):
    return render(request, 'furniture/detail.html')

def pricing(request):
    return render(request, 'furniture/pricing.html')

def shop(request):
    DTproducts = Product.objects.all()
    context = {
        'Objproducts': DTproducts
    }
    return render(request, 'furniture/shop.html', context)

def teamDetail(request):
    return render(request, 'furniture/team_detail.html')

def team(request):
    return render(request, 'furniture/team.html')
