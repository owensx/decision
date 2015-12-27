# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='idea',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('status', models.CharField(choices=[('A', 'Agreed'), ('D', 'Disagree'), ('C', 'Counter'), ('P', 'Pending')], max_length=1)),
                ('description', models.CharField(max_length=99)),
                ('statement', models.CharField(max_length=99)),
                ('opinion', models.CharField(max_length=99)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
