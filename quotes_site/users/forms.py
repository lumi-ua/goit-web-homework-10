from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    
    first_name = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}))
    
    last_name = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}))
    
    email = forms.EmailField(max_length=100,
                            required=True,
                            widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    
    password1 = forms.CharField(max_length=20,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    
    password2 = forms.CharField(max_length=20,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))

    password = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))


    class Meta:
        model = User
        fields = ['username', 'password']

