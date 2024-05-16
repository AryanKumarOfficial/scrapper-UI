from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ScrapForm
from .models import URLModel, scrappedDataModel
from home.BACKEND.MODULES.setup import setup
import os


def Scrapping(request):
    url = URLModel.objects.all().order_by('-created_at').first()
    scrapped_data = setup(url.url)
    print(scrapped_data, "scrapped_data")
    sd = scrappedDataModel.objects.create(
        url=url,
        words_collection=scrapped_data[0],
        unique_words_count=scrapped_data[1],
        total_words_count=scrapped_data[2],
        title=scrapped_data[3],
        total_reviews=scrapped_data[4]
    )
    if os.path.exists("data"):
        os.system("rm -r data")
    context = {
        'url': url,
        'scrapped_data': scrapped_data
    }
    return render(request, 'data.html', context)


def Data(request):
    return render(request, 'data.html')


def Loader(request):
    context = {}
    # render the lodader.html then run the scrapping function
    render(request, 'loader.html', context)
    return redirect('scrapping')


def home(request):
    context = {}
    if request.method == "POST":
        form = ScrapForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # Save URL to the database
            URLModel.objects.create(url=url)
            context['url'] = url
            print(url, "url_instance")
            # Redirect to the loader view
            return redirect('loader')
    else:
        form = ScrapForm()
    context['form'] = form
    return render(request, 'index.html', context)
