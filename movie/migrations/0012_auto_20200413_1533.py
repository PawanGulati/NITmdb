# Generated by Django 3.0.5 on 2020-04-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20200413_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='carousal_pic1',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='carousal_pic2',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='carousal_pic3',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
