#!/usr/bin/env python2

from django.db import models


class Action(models.Model):
    goal = models.ForeignKey('Goal', verbose_name=u"Goal", related_name="actions")
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

