# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
    ]