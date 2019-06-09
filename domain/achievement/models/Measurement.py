#!/usr/bin/env python2

from django.db import models


class Measurement(models.Model):
    action = models.ForeignKey('Action', verbose_name=u"Action", related_name='measurements')
    intention = models.ForeignKey('Intention', verbose_name=u"Intention", related_name='measurements')
    outcome_metric = models.FloatField(u"Outcome Metric", help_text='How much/many times did you perform the action?')
    enjoyable_aspects = models.TextField(u"Easy Aspects", blank=True, help_text='What did you enjoy about doing this today?')
    difficult_aspects = models.TextField(u"Difficult Aspects", blank=True, help_text='What did you find difficult about doing this today?')
    overcoming_difficult_aspects = models.TextField(u"Overcome Difficult Aspects", blank=True, help_text='How did you overcome the difficulties?')
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    class Meta:
        verbose_name = u"Measurement"
        verbose_name_plural = u"Measurements"
        ordering = ("created_date", "action",)

    def __unicode__(self):
        return u"%s" % (self.created_date)
