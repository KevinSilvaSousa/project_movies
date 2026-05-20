from django.contrib import admin
from django.urls import path

from movies.views import criar_movies, get_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', criar_movies),
    path('pegar_filme/<int:id>', get_movies),
]
