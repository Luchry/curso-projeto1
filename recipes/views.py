from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path


def home(request):

    return render(request, 'recipes/home.html', context={
        'name': 'lucas soares',
    })


def about(request):

    return HttpResponse('ABOUT')


def contact(request):

    return render(request, 'recipes/contact.html', context={
        'telefone': '13997861119',
    })

# Create your views here.
