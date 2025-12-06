from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    path('indexFur/', views.indexFur, name='indexFur'),
    path('aboutFur/', views.indexFur, name='aboutFur'),
    path('blogDetial/', views.indexFur, name='blogDetial'),
    path('blog/', views.indexFur, name='blog'),
    path('cart/', views.indexFur, name='cart'),
    path('checkOut/', views.indexFur, name='checkOut'),
    path('contact/', views.indexFur, name='contact'),
    path('detail/', views.indexFur, name='detail'),
    path('pricing/', views.indexFur, name='pricing'),
    path('shop/', views.indexFur, name='shop'),
    path('teamDetail/', views.indexFur, name='teamDetail'),
    path('team/', views.indexFur, name='team')
]