#!/usr/bin/env python2

from django.db import models


class Goal(models.Model):
    parent_goal = models.ForeignKey('Goal', verbose_name=u"Parent Goal", related_name="subgoals", null=True)
    verb = models.CharField(
        u"Verb",
        max_length=300,
        help_text='Which action do you perform to satisfy this goal? For example, "Complete"'
    )
    verb_phrase = models.CharField(
        u"Verb Phrase",
        max_length=500,
        help_text='A verb phrase which captures the object of the verb and any qualifiers. For example, "my Chemistry revision"'
    )
    target_date = models.DateField('Target Date', help_text='The date by which you want to have achieved this goal')
    end_state_description = models.TextField(
        "End State Description",
        help_text='Describe what it looks like when you have achieved the goal',
        blank=True
    )
    urgency = models.FloatField('Urgency', null=True) # TODO eisenhower ordering 17/05/2020 10:41: Add mix/max constraints
    importance = models.FloatField('Importance', null=True) # TODO eisenhower ordering 17/05/2020 10:41: Add mix/max constraints
    complete = models.BooleanField(u"Complete?", default=False)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    def __unicode__(self):
        return u"%s" % (self.title)

    @property
    def title(self):
        return '{} {} by {}'.format(self.verb, self.verb_phrase, self.target_date)

    @property
    def eisenhower_score(self):
        return (self.urgency * self.importance) / 100

    class Meta:
        verbose_name = u"Goal"
        verbose_name_plural = u"Goals"

