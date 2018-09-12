# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pelicula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='etiqueta',
            field=models.CharField(max_length=150, default=datetime.datetime(2018, 4, 9, 15, 59, 8, 84303, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
