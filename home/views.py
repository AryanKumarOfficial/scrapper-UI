from django.shortcuts import render, redirect
from .forms import ScrapForm


def home(request):
    context = {}
    if request.method == "POST":
        form = ScrapForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            context['url'] = url
            return render(request, 'data.html', context)
    else:
        form = ScrapForm()
    context['form'] = form
    return render(request, 'index.html', context)


def Data(request):
    return render(request, 'data.html')
