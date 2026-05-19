from django.db import models

# Create your models here.


class MoviesModel(models.Model):
    movies = models.CharField(max_length=1000)
    ano_lascamento = models.IntegerField()
    genero = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.movies