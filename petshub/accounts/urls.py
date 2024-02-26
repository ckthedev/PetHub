from django.urls import path
from .views import register, login, logout, profile, account_options

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
     path('account-options/', account_options, name='account_options'),
]
