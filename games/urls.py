from django.urls import path, include
from . import views
from .views import UserProfile, CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/profile/', UserProfile.as_view(), name='profile'),
]

