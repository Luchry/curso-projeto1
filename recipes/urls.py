from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('sobre/', about),
    path('', home),
    path('contato/', contact),

]
