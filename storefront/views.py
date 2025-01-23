from django.shortcuts import render

def home(request):
    context = {'message': 'Hello, Django!'}
    return render(request, 'home/home.html', context)

def wishlist(request):
    return render(request, 'wishlist.html', context={
        'authPage': 'Wishlist'
    } )

def cart(request):
    return render(request, 'cart.html', context={
        'authPage': 'Cart'
    } )

def shop(request):
    return render(request, 'shop.html', context={
        'authPage': 'Shop'
    })

def login(request):
    return render(request, 'auth/login.html', context={
        'authPage': 'Login'
    } )
    
def register(request):
    return render(request, 'auth/register.html', context={
        'authPage': 'Register'
    } )

def forget(request):
    return render(request, 'forget.html', context={
        'authPage': 'Forget'
    })

def account(request):
    return render(request, 'accounts.html', context={
        'authPage': 'Account'
    })