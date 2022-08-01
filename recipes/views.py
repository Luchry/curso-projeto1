from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home(request):

    return render(request, 'recipes/pages/home.html', context={
        'name': 'lucas soares',
    })


def recipe(request, id):

    return render(request, 'recipes/pages/home.html', context={
        'name': 'lucas soares',
    })


# Create your views here.
