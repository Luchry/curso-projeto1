from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home(request):

    return render(request, 'recipes/home.html', context={
        'name': 'lucas soares',
    })


# Create your views here.
