from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    

class LoginForm(forms.Form):
    """User login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegistrationForm(UserCreationForm):
    """User registration form"""
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        

def clean_email(self):
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')
    if User.objects.filter(email=email).exclude(username=username):
        raise forms.ValidationError(u'This email is already registered.')
    return email


def clean_password(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if not password1 or not password2:
        raise forms.ValidationError(u'Please confirm your password.')
    if password1 != password2:
        raise forms.ValidationError(u'Passwords must match.')
    return password2


    
    