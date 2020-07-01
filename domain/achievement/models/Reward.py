#!/usr/bin/env python2

from django.db import models


class Reward(models.Model):
    goal = models.ForeignKey('Goal', verbose_name=u"Reward", related_name='rewards')
    reward_title = models.CharField(u"Reward Title", max_length=1000)
    reward_description = models.TextField(u"Reward Description", blank=True,
                                          help_text='Describe what the reward is - make it sound inviting')
    achievement_metric = models.FloatField(u"Achievement Metric",
                                           help_text='This is the metric amount you must attain to get the reward')
    obtained = models.BooleanField(u"Reward Obtained?", default=False)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)



    class Meta:
        verbose_name = u"Reward"
        verbose_name_plural = u"Rewards"
        ordering = ("goal", "achievement_metric", "obtained")

    def __unicode__(self):
        return u"%s" % (self.reward_title)
