from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Product, CarouselSlide, AboutHeroImages
from accounts.models import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def indexFur(request):
    # 1. Fetch all carousel slides, ordered by the 'order' field
    slides = CarouselSlide.objects.all() 
    
    # 2. Fetch the AboutHeroImages object
    # We use .first() because we expect only one entry for this single-instance model
    about_images = AboutHeroImages.objects.first() 
    
    context = {
        'slides': slides,
        'about_images': about_images,  # Pass the About images object to the template
    }
    return render(request, 'furniture/index.html', context)

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
