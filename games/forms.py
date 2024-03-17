from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import UserProfile

class SignUpForm(UserCreationForm):
    #email = forms.EmailField() #i am not sure about this one will have to run it then i can change it later
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birthday']  # Specify the fields you want to include in the form
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),  # Optional: customize widget attributes
            'birthday': forms.DateInput(attrs={'type': 'date'})  # Optional: customize widget attributes
        }