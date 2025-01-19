from django import forms
from .models import Product
from django.forms import ModelForm
from django.contrib.auth.models import Group


class Group_form(ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'prise', 'discount', 'description'

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()