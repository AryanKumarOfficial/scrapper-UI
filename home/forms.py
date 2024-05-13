# forms.py
from django import forms
from .models import ScrapFormModel


class ScrapForm(forms.Form):
    url = forms.URLField(label='URL', max_length=1000)
