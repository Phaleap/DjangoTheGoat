from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),

    path('indexFur/', views.indexFur, name='indexFur'),
    path('aboutFur/', views.aboutFur, name='aboutFur'),
    path('blogDetail/', views.blogDetial, name='blogDetail'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='shoppingcart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shopdetail/', views.detail, name='shopdetail'),
    path('pricing/', views.pricing, name='pricing'),
    path('shop/', views.shop, name='shop'),
    path('teamDetail/', views.teamDetail, name='teamDetail'),
    path('team/', views.team, name='team'),
   
]
