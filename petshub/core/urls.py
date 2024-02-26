from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('community/', views.community, name='community'),
    path('blog/', views.blog, name='blog'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
     path('account/', views.account_page, name='account_page'),
    
]
