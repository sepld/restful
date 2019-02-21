# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='book',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='book',
            name='style',
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
