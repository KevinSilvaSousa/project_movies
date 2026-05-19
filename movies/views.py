from django.shortcuts import render
from django.http import HttpResponse



def view_movies(request):
    return HttpResponse ("Pagina de filmes")


def l