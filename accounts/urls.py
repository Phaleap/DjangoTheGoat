from django.urls import path, include
from . import views
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('blog/', views.blog_list_view, name='blog'),
    path('', views.indexFur, name='indexFur'),
    path('aboutFur/', views.aboutFur, name='aboutFur'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('cart/', views.cart, name='shoppingcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shopdetail/<int:id>/', views.detail, name='detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('shop/', views.shop, name='shop'),
    path('team_detail/<int:id>/', views.team_detail, name='team_detail'),
    path('team/', views.team, name='team'),
    path('blog/category/<slug:slug>/', views.blogCategory, name='blog_category_detail'),
    path('blog/tag/<slug:slug>/', views.blogTag, name='blog_tag_detail'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('billing_list/', views.billing_list, name='billing_list'),
    path('billing/add/', views.billing_add, name='billing_add'), 
    path('BillingList/', views.billing_list, name='BillingList'),
    path('shopping-cart/', views.shopping_cart, name='shoppingcart'),
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path("save_contact/", views.save_contact, name="save_contact"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
