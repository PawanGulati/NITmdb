from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy
# from django.core import validators
# from django.core.validators import MaxLengthValidator, MinLengthValidator

# resizing image pillow
from PIL import Image
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
    poster_image = models.ImageField(default='images/default.jpg', upload_to='images')
    genre = models.CharField(choices=GENRE, max_length=7, null=True)
    language = models.CharField(choices=LANGUAGE, max_length=7, null=True)
    release_date = models.DateTimeField(default=timezone.now)
    IMDB_rating = models.FloatField(default=0,)
    director = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cast = models.CharField(max_length=100, null=True)

    carousal_pic1 = models.ImageField(
        default='default.jpg', upload_to='images')
    carousal_pic2 = models.ImageField(
        default='default.jpg', upload_to='images')
    carousal_pic3 = models.ImageField(
        default='default.jpg', upload_to='images')

    def truncate_str(self):
        return self.description[0:100] + ' ....'

    # redirection after creation of movie
    def get_absolute_url(self, **kwargs):
        return reverse_lazy('movie_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.movie_name

    # implementing image resizing
    def save(self):
        super().save()
        img = Image.open(self.poster_image.path)
        if img.height > 100 or img.width > 100:
            print(0)
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.poster_image.path)

# TODO will see if get time to do


class Review(models.Model):
    pass


class Comment(models.Model):
    pass


class Download_link(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='links', null=True)
    link = models.URLField(default='#')
