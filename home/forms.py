# forms.py
from django import forms


class ScrapForm(forms.Form):
    url = forms.URLField(
        label='URL',  max_length=1000)
