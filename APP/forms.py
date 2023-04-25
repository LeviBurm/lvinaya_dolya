from django import forms
from .models import * 

class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryPostForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ClientPostForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']