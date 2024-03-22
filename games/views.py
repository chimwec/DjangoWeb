from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import UserProfileForm
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

# Create your views here.
#@login_required
def home(request):
    context = {"name": request.user}
    return render(request, 'games/home.html', context)

@login_required
def about(request):
    context = {"name": "chim"}
    return render(request, 'games/about.html', context)

# Registers a new user account.
#
# If the request method is POST, validates the form data and creates a new user.
# The form contains username, email, and password fields. 
# After successful validation, the user is logged in automatically.
#
# If the request method is GET, displays a blank registration form.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #we create the user object
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1') #Hash password
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('games/register.html')
    else:
         form = SignUpForm()
    return render(request, 'games/register.html', {'form': form})  

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "games/register.html"


        
class CustomLoginView(LoginView):
    template_name = 'games/login.html'
    success_url = 'home.html'
    extra_context = {'login': 'active'}

    def form_invalid(self, form):
        return HttpResponse("Invalid credentials")
    


def logout_request(request):
    logout(request)
    return redirect("home")


class UserProfile(LoginRequiredMixin,CreateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy("home")
    template_name = "games/profile.html"
   