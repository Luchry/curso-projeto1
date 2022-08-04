from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home(request):

    return render(request, 'recipes/pages/home.html', context={
        'name': 'lucas soares',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
    })


# Create your views here.
