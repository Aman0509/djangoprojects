from django import forms
from .models import NewUsers

class NewUsersForm(forms.ModelForm):
    class Meta:
        model = NewUsers
        fields = '__all__'
    
        widget = {
        'fname': forms.TextInput(attrs={'class':'form-element', 'placeholder':'First Name'}),
        'lname': forms.TextInput(attrs={'class':'form-element','placeholder':'Last Name'}),
        'phone_number': forms.TextInput(attrs={'class':'form-element', 'placeholder':'Phone Number'}),
        'email': forms.EmailInput(attrs={'class':'form-element','placeholder':'Email'}),
    }