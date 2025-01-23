from django.shortcuts import render

def home(request):
    context = {'message': 'Hello, Django!'}
    return render(request, 'index.html', context)

def wishlist(request):
    return render(request, 'wishlist.html')

def cart(request):
    return render(request, 'cart.html')

def shop(request):
    return render(request, 'shop.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'auth/register.html', context={
        'authPage': 'Register'
    } )

def forget(request):
    return render(request, 'forget.html')