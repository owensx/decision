# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_idea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='opinion',
            field=models.CharField(blank=True, max_length=99),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='idea',
            name='status',
            field=models.CharField(choices=[('AGREED', 'Agreed'), ('DISAGREE', 'Disagree'), ('COUNTER', 'Counter'), ('PENDING', 'Pending')], max_length=99),
            preserve_default=True,
        ),
    ]
