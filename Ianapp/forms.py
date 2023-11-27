# jibmbe_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']

class LocationRequestForm(forms.Form):
    # Form for requesting nearby events/hotels
    pass
class LocationRequestForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    
class AvatarForm(forms.Form):
    # Define your form fields here
    avatar = forms.ImageField()

class LocationForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    # Ianapp/forms.py
from django import forms

class BioForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

    
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    

