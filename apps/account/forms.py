from django import forms
from .models import People

class FileForm(forms.Form):
    file = forms.FileField()
