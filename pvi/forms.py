from multiprocessing.sharedctypes import Value
from django import forms 
from .models import item1, item2

class ItemForm1(forms.ModelForm):
    class Meta:
        model = item1
        fields = ['ins_municipal1']

class ItemForm2(forms.ModelForm):
    class Meta:
        model = item2
        fields = ['ins_municipal2']