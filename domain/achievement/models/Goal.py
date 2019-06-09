#!/usr/bin/env python2

from django.db import models


class Goal(models.Model):
    title = models.CharField(u"Title", max_length=200)
    end_state_description = models.TextField(
        "End State Description",
        help_text='Describe what it looks like when you have achieved the goal',
        blank=True
    )
    target_date = models.DateField('Target Date', help_text='The date by which you want to have achieved this goal')
    complete = models.BooleanField(u"Complete?", default=False)
    # owner = models.ForeignKey('User', verbose_name=u"User", related_name="goals", blank=True, null=True)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    class Meta:
        verbose_name = u"Goal"
        verbose_name_plural = u"Goals"
        # ordering = ("-sticky", "-date",)

    def __unicode__(self):
        return u"%s" % (self.title)
