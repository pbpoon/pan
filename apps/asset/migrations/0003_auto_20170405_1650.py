# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('asset', '0002_auto_20170405_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='people',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='owner',
            unique_together=set([('owner', 'num')]),
        ),
    ]
