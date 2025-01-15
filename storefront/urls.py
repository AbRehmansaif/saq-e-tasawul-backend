from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('wishlist.html', views.wishlist, name='wishlist'),
    path('cart.html', views.cart, name='cart'),
    path('shop.html', views.shop, name='shop'),
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('forget.html', views.forget, name='forget'),
]
