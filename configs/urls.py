from django.contrib import admin
from django.urls import path

from movies.views import view_movies, get_movies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', view_movies),
    path('pegar_filme/<int:id>', get_movies),
]
