from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from home.BACKEND.MODULES.setup import setup


def home(request):

    return render(request, "index.html")


def scrap(request):
    data = request.POST.get("url")
    print(data)

    return render(request, "index.html")
