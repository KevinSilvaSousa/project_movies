from django.contrib import admin
from django.urls import path, include

from movies.views import criar_movies, get_movies, inicio

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('pegar_filme/<int:id>', get_movies),
]
