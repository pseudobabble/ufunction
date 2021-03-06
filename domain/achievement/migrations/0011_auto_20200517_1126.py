# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-05-17 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0010_auto_20200517_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ('target_date', 'urgency', 'importance', 'eisenhower_score'), 'verbose_name': 'Goal', 'verbose_name_plural': 'Goals'},
        ),
        migrations.RemoveField(
            model_name='goal',
            name='stative_verb',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='status',
        ),
        migrations.AddField(
            model_name='goal',
            name='verb',
            field=models.CharField(default='Complete', help_text=b'Which action do you perform to satisfy this goal? For example, "Complete"', max_length=300, verbose_name='Verb'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='verb_phrase',
            field=models.CharField(default='Chemistry Revision Chapters 1-3', help_text=b'A verb phrase which captures the object of the verb and any qualifiers. For example, "my Chemistry revision"', max_length=500, verbose_name='Verb Phrase'),
            preserve_default=False,
        ),
    ]
