#!/usr/bin/env python2

from django.db import models


class Goal(models.Model):
    stative_verb = models.CharField(
        u"Stative Verb",
        max_length=300,
        help_text='A Stative Verb which expresses the end state of the goal, ie: have, be, know, like'
    )
    status = models.CharField(
        u"Status",
        max_length=500,
        help_text='A Predicate Noun which expresses the status of the goal'
    )
    target_date = models.DateField('Target Date', help_text='The date by which you want to have achieved this goal')
    end_state_description = models.TextField(
        "End State Description",
        help_text='Describe what it looks like when you have achieved the goal',
        blank=True
    )
    complete = models.BooleanField(u"Complete?", default=False)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    def __unicode__(self):
        return u"%s" % (self.title)

    @property
    def title(self):
        return '{} {} {}'.format(self.stative_verb, self.status, self.target_date)

    class Meta:
        verbose_name = u"Goal"
        verbose_name_plural = u"Goals"
        # ordering = ("-sticky", "-date",)

