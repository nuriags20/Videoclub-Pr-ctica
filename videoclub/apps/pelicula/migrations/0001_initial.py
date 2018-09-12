# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=150)),
                ('video', models.URLField()),
                ('descripcion', models.TextField()),
                ('año', models.IntegerField()),
                ('director', models.CharField(max_length=150)),
                ('reparto', models.CharField(max_length=150)),
                ('portada', models.URLField()),
                ('valoracion', models.IntegerField()),
            ],
        ),
    ]
