# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0002_pelicula_etiqueta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='etiqueta',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.URLField(max_length=350),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='reparto',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='valoracion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='video',
            field=models.URLField(max_length=350),
        ),
    ]
