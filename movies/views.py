from django.shortcuts import render
from django.http import HttpResponse
from .models import MoviesModel



def view_movies(request, lista):
    return HttpResponse ("Pagina de filmes")


def get_movies(request, id):
    filme = MoviesModel.objects.get(id=id)
    return HttpResponse (filme)

def list_movies(request):
    filme = MoviesModel.objects.filter(id)
    return HttpResponse (filme)
