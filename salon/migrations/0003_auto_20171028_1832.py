# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_auto_20171015_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(default='media/images/employees/no-img.jpg', upload_to='media/images/employees/'),
        ),
    ]
