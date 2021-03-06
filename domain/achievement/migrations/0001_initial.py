# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-08 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(help_text=b'What action is this?', max_length=500, verbose_name='Action')),
                ('target_metric', models.FloatField(help_text=b'How will you know if you have done this enough to achieve the goal?', verbose_name='Target')),
                ('target_metric_unit', models.CharField(help_text=b'The units of your target metric', max_length=500, verbose_name='Unit')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('end_state_description', models.TextField(blank=True, help_text=b'Describe what it looks like when you have achieved the goal', verbose_name=b'End State Description')),
                ('target_date', models.DateField(help_text=b'The date by which you want to have achieved this goal', verbose_name=b'Target Date')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
        ),
        migrations.CreateModel(
            name='Intention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intention', models.CharField(help_text=b'What will you do today to bring you closer to your goal?', max_length=1000, verbose_name='Todays Intention')),
                ('intended_metric', models.FloatField(help_text=b'How much/many times will you perform the action?', verbose_name='Intended Metric')),
                ('enjoyable_aspects', models.CharField(max_length=1000, verbose_name='What do you enjoy about this activity?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentions', to='achievement.Action', verbose_name='Action')),
            ],
            options={
                'ordering': ('created_date', 'action'),
                'verbose_name': 'Intention',
                'verbose_name_plural': 'Intentions',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outcome_metric', models.FloatField(help_text=b'How much/many times did you perform the action?', verbose_name='Outcome Metric')),
                ('enjoyable_aspects', models.TextField(blank=True, help_text=b'What did you enjoy about doing this today?', verbose_name='Easy Aspects')),
                ('difficult_aspects', models.TextField(blank=True, help_text=b'What did you find difficult about doing this today?', verbose_name='Difficult Aspects')),
                ('overcoming_difficult_aspects', models.TextField(blank=True, help_text=b'How did you overcome the difficulties?', verbose_name='Overcome Difficult Aspects')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='achievement.Action', verbose_name='Action')),
                ('intention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='achievement.Intention', verbose_name='Intention')),
            ],
            options={
                'ordering': ('created_date', 'action'),
                'verbose_name': 'Measurement',
                'verbose_name_plural': 'Measurements',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_period', models.CharField(choices=[(b'WEEKLY', b'Weekly'), (b'MONTHLY', b'Monthly'), (b'QUARTERLY', b'Quarterly'), (b'ANNUAL', b'Annual')], max_length=500, verbose_name='Review Period')),
                ('review_period_start_date', models.DateField(blank=True, verbose_name='Date (Create)')),
                ('review_period_end_date', models.DateField(blank=True, verbose_name='Date (Update)')),
                ('enjoyable_aspects', models.TextField(blank=True, help_text=b'What was enjoyable about working towards this goal?', verbose_name='Easy Aspects')),
                ('difficult_aspects_text', models.TextField(blank=True, help_text=b'What was difficult about working towards this goal?', verbose_name='Difficult Aspects')),
                ('overcome_difficult_aspects_text', models.TextField(blank=True, help_text=b'What worked to overcome the difficulties', verbose_name='Overcome Difficult Aspects')),
                ('next_period_focus', models.TextField(blank=True, help_text=b'What do you need to focus on in the next period?', verbose_name='Next Period Focus')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='achievement.Goal', verbose_name='Goal Review')),
            ],
            options={
                'ordering': ('goal', 'review_period_end_date'),
                'verbose_name': 'Goal Review',
                'verbose_name_plural': 'Goal Reviews',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_title', models.CharField(max_length=1000, verbose_name='Reward Title')),
                ('reward_description', models.TextField(blank=True, help_text=b'Describe what the reward is - make it sound inviting', verbose_name='Reward Description')),
                ('achievement_metric', models.FloatField(help_text=b'This is the metric amount you must attain to get the reward', verbose_name='Achievement Metric')),
                ('obtained', models.BooleanField(default=False, verbose_name='Reward Obtained?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='achievement.Goal', verbose_name='Reward')),
            ],
            options={
                'ordering': ('goal', 'achievement_metric', 'obtained'),
                'verbose_name': 'Reward',
                'verbose_name_plural': 'Rewards',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(help_text=b'What is the theme of this goal, eg Health, Wealth, etc', max_length=500, verbose_name=b'Theme')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='achievement.Goal', verbose_name='Goal')),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='achievement.Goal', verbose_name='Goal'),
        ),
    ]
