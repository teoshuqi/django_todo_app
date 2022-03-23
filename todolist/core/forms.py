from django import forms
from .models import toDo

class ItemForm(forms.ModelForm):
    name = forms.CharField(required=True)
    class Meta:
        model = toDo
        exclude = ["status"]

