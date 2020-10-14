from django import forms


class ItemForm(forms.Form):
    name = forms.CharField(max_length=50)
    quantity = forms.IntegerField(max_value=1000)
