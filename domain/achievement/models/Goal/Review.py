#!/usr/bin/env python2

from django.db import models

REVIEW_PERIOD_CHOICES = (
    ('WEEKLY', 'Weekly'),
    ('MONTHLY', 'Monthly'),
    ('QUARTERLY', 'Quarterly'),
    ('ANNUAL', 'Annual'),
)


class Review(models.Model):
    goal = models.ForeignKey('Goal', verbose_name=u"Goal Review", related_name='reviews')
    review_period = models.CharField(u"Review Period", choices=REVIEW_PERIOD_CHOICES, max_length=500)
    review_period_start_date = models.DateField(u"Date (Create)", blank=True)
    review_period_end_date = models.DateField(u"Date (Update)", blank=True)
    enjoyable_aspects = models.TextField(u"Easy Aspects", blank=True, help_text='What was enjoyable about working towards this goal?')
    difficult_aspects_text = models.TextField(u"Difficult Aspects", blank=True, help_text='What was difficult about working towards this goal?')
    overcome_difficult_aspects_text = models.TextField(u"Overcome Difficult Aspects", blank=True, help_text='What worked to overcome the difficulties')
    next_period_focus = models.TextField(u"Next Period Focus", blank=True, help_text='What do you need to focus on in the next period?')
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    class Meta:
        verbose_name = u"Goal Review"
        verbose_name_plural = u"Goal Reviews"
        ordering = ("goal", "review_period_end_date",)

    def __unicode__(self):
        return u"%s" % (self.review_period_end_date)
