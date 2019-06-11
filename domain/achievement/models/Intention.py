#!/usr/bin/env python2
from django.db import models


class Intention(models.Model):
    action = models.ForeignKey('Action', verbose_name=u"Action", related_name="intentions")
    intention_text = models.CharField(u"Todays Intention", max_length=1000, help_text='What will you do today to bring you closer to your goal?')
    intended_metric = models.FloatField(u"Intended Metric", help_text='How much/many times will you perform the action?')
    enjoyable_aspects = models.CharField(u"What do you enjoy about this activity?", max_length=1000)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    class Meta:
        verbose_name = u"Intention"
        verbose_name_plural = u"Intentions"
        ordering = ("created_date", "action",)

    def __unicode__(self):
        return u"%s" % (self.created_date)
