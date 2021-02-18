from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    contact_number = forms.CharField(min_length=10,max_length=10)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','contact_number','password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
        }
