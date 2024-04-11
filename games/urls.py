from django.urls import path, include
from . import views
from .views import UserProfile, CustomLoginView, Register, logout_request

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_request, name='logout'),
    path('accounts/profile/', UserProfile.as_view(), name='profile'),
]

