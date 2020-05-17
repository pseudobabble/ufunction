# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-05-17 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0006_goal_parent_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intention',
            name='action',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='action',
        ),
        migrations.AddField(
            model_name='intention',
            name='goal',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='intentions', to='achievement.Goal', verbose_name='Goal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurement',
            name='goal',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='achievement.Goal', verbose_name='Goal'),
            preserve_default=False,
        ),
    ]
