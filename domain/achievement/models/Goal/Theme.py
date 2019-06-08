#!/usr/bin/env python2

from django.db import models


class Theme(models.Model):
    goal = models.ForeignKey('Goal', verbose_name=u"Goal", related_name="themes")
    theme = models.CharField('Theme', max_length=500, help_text='What is the theme of this goal, eg Health, Wealth, etc')


