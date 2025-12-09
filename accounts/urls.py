from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('blog/', views.blog_list_view, name='blog'),
    path('indexFur/', views.indexFur, name='indexFur'),
    path('aboutFur/', views.aboutFur, name='aboutFur'),
    path('blogDetail/<int:id>/', views.blogDetial, name='blogDetail'),
    path('cart/', views.cart, name='shoppingcart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shopdetail/<int:pk>/', views.detail, name='detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('shop/', views.shop, name='shop'),
    path('team_detail/<int:id>/', views.team_detail, name='team_detail'),
    path('team/', views.team, name='team'),
    path('blog/<int:id>/', views.blogDetial, name='blog_detail'),
    path('blog/category/<slug:slug>/', views.blogCategory, name='blog_category_detail'),
    path('blog/tag/<slug:slug>/', views.blogTag, name='blog_tag_detail'),
]
