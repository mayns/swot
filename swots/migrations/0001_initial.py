# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagram',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('strengths', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=200))),
                ('weaknesses', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=200))),
                ('opportunities', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=200))),
                ('threats', django.contrib.postgres.fields.ArrayField(size=None, base_field=models.TextField(max_length=200))),
            ],
        ),
    ]
