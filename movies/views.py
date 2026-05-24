from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MoviesModel


def inicio(request):
    return render (request, 'inicio.html')

def criar_movies(request):
    if request.method == 'GET':
        movie = MoviesModel.objects.all()
        print(movie)
        return HttpResponse ("Pagina de filmes")

    
    elif request.method == 'POST':
        movies = MoviesModel(name=movies)
        movies.save()
        return redirect ('criar_movies')
    



def get_movies(request, id):
    filme = MoviesModel.objects.get(id=id)
    return HttpResponse (filme)

def list_movies(request):
    filme = MoviesModel.objects.filter(id)
    return HttpResponse (filme)
