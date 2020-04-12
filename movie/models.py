from django.db import models
from django.contrib.auth.models import User

# Create your models here.to, on_delete


class Movie(models.Model):
    GENRE = (
        ('ACTION', 'ACTION'),
        ('DRAMA', 'DRAMA'),
        ('CRIME', 'CRIME'),
        ('COMEDY', 'COMEDY'),
        ('ROMANCE', 'ROMANCE'),
        ('MYSTERY', 'MYSTERY'),
    )
    LANGUAGE = (
        ('EN', 'English'),
        ('HN', 'Hindi'),
        ('FR', 'French'),
        ('CH', 'Chineese'),
        ('KO', 'Korean'),
    )

    movie_name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)
    poster_image = models.ImageField(upload_to='movies', null=True)
    genre = models.CharField(choices=GENRE, max_length=7, null=True)
    language = models.CharField(choices=LANGUAGE, max_length=7, null=True)
    release_date = models.DateTimeField(null=True)
    IMDB_rating = models.FloatField(default=0)
    director = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.movie_name
