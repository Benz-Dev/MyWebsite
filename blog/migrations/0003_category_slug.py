# Generated by Django 3.1.7 on 2021-03-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210314_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='null', verbose_name='Clase'),
        ),
    ]
