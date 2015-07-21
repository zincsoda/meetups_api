# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('image_url', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('meeting_time', models.TextField(null=True, blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('postcode', models.CharField(max_length=12, null=True, blank=True)),
                ('contact', models.CharField(max_length=200, null=True, blank=True)),
                ('website', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='meetups.Image', null=True)),
            ],
        ),
    ]
