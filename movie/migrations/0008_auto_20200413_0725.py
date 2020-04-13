# Generated by Django 3.0.5 on 2020-04-13 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200413_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='IMDB_rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(0)]),
        ),
    ]