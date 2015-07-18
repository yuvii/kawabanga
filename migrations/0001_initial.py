# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import banga.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dough',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd7\xa9\xd7\x9d')),
            ],
            options={
                'verbose_name': '\u05d1\u05e6\u05e7',
                'verbose_name_plural': '\u05d1\u05e6\u05e7\u05d9\u05dd',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd7\xa9\xd7\x9d')),
                ('description', models.TextField(verbose_name=b'\xd7\xaa\xd7\x99\xd7\x90\xd7\x95\xd7\xa8')),
                ('position', models.IntegerField(verbose_name=b'\xd7\x9e\xd7\x99\xd7\xa7\xd7\x95\xd7\x9d')),
                ('dough', models.ForeignKey(verbose_name=b'\xd7\x91\xd7\xa6\xd7\xa7', to='banga.Dough')),
            ],
            options={
                'verbose_name': '\u05e4\u05d9\u05e6\u05d4',
                'verbose_name_plural': '\u05e4\u05d9\u05e6\u05d5\u05ea',
            },
        ),
        migrations.CreateModel(
            name='PizzaImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=banga.models.img_uploader, verbose_name=b'\xd7\xaa\xd7\x9e\xd7\x95\xd7\xa0\xd7\x94')),
                ('pizza', models.ForeignKey(related_name='images', verbose_name=b'\xd7\xa4\xd7\x99\xd7\xa6\xd7\x94', to='banga.Pizza')),
            ],
            options={
                'verbose_name': '\u05ea\u05de\u05d5\u05e0\u05d4 \u05dc\u05e4\u05d9\u05e6\u05d4',
                'verbose_name_plural': '\u05ea\u05de\u05d5\u05e0\u05d5\u05ea \u05dc\u05e4\u05d9\u05e6\u05d4',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd7\xa9\xd7\x9d')),
            ],
            options={
                'verbose_name': '\u05ea\u05d5\u05e1\u05e4\u05ea',
                'verbose_name_plural': '\u05ea\u05d5\u05e1\u05e4\u05d5\u05ea',
            },
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='banga.Topping', verbose_name=b'\xd7\xaa\xd7\x95\xd7\xa1\xd7\xa4\xd7\x95\xd7\xaa'),
        ),
    ]
