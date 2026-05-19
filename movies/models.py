from django.db import models

# Create your models here.


class MoviesModel(models.Model):
    movies = models.CharField(max_length=1000, min_length=1)
    ano_lascamento = models.IntegerField()
    genero = models.CharField(max_length=1000, min_length=1)
    