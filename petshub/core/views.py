from django.views import View
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def community(request):
    return render(request, 'community.html')

def blog(request):
    return render(request, 'blog.html')

def account_page(request):
    # Add any logic needed for the account page here
    return render(request, 'account_page.html')

    
def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')
