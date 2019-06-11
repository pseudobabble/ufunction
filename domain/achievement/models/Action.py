#!/usr/bin/env python2

from django.db import models

from model_utils import Choices


class Action(models.Model):
    ACTION_VERBS = Choices(
        ('Increase', 'Increase'),
        ('Reduce', 'Reduce'),
        ('Maintain', 'Maintain'),
    )
    goal = models.ForeignKey('Goal', verbose_name=u"Goal", related_name="actions")
    action_verb = models.CharField(
        u"Action Verb",
        max_length=100,
        choices=ACTION_VERBS,
        default=ACTION_VERBS.Increase,
        help_text='What action is this?'
    )
    activity = models.CharField(
        u"Activity",
        max_length=300,
        help_text='This should be the activity which moves you towards the goal, expressed as a nominalisation, eg calorie intake'
    )
    target_metric = models.FloatField(u"Target", help_text='How will you know if you have done this enough to achieve the goal?')
    target_metric_unit = models.CharField(u"Unit", max_length=500, help_text='The units of your target metric')
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    class Meta:
        verbose_name = u"Action"
        verbose_name_plural = u"Actions"
        # ordering = ("-sticky", "-date",)

    def __unicode__(self):
        return u"%s" % (self.action_verb)
