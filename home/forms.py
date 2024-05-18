# forms.py
from django import forms
from .models import URLModel


class ScrapForm(forms.Form):
    class Meta:
        model = URLModel
        fields = ['url']
    url = forms.URLField(
        label='URL',  max_length=1000)
