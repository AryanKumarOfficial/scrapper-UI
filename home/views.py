from django.shortcuts import render, redirect
from .forms import ScrapForm
from .models import URLModel,scrappedDataModel
from home.BACKEND.MODULES.setup import setup


def home(request):
    context = {}
    if request.method == "POST":
        form = ScrapForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # scrappd_data = (words_collection, unique_words_count, total_words_count, title, total_reviews)
            scrapped_data = setup(url)
            sd = scrappedDataModel.objects.create(
                url=url,
                words_collection=scrapped_data[0],
                unique_words_count=scrapped_data[1],
                total_words_count=scrapped_data[2],
                title=scrapped_data[3],
                total_reviews=scrapped_data[4]
            )
            context['url'] = url
            return render(request, 'data.html', context)
    else:
        form = ScrapForm()
    context['form'] = form
    return render(request, 'index.html', context)


def Data(request):
    return render(request, 'data.html')
