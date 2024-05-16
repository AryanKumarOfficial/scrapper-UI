from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loader/', views.Loader, name='loader'),
    path('scrapping/', views.Scrapping, name='scrapping'),
    path('data/', views.Data, name='data'),
]
