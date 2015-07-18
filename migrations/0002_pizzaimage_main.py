# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaimage',
            name='main',
            field=models.BooleanField(default=1, verbose_name=b'\xd7\xa2\xd7\x99\xd7\xa7\xd7\xa8\xd7\x99'),
            preserve_default=False,
        ),
    ]
