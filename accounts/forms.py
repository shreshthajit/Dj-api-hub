from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
           email = forms.EmailField(required=True)
           phone_number = forms.CharField(max_length=15, required=False)
           role = forms.ChoiceField(choices=CustomUser.ROLES, required=True)

           class Meta:
               model = CustomUser
               fields = ('username', 'email', 'phone_number', 'role', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
           class Meta:
               model = CustomUser
               fields = ('username', 'password')