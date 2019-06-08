#!/usr/bin/env python2
from django.db import models


class Intention(models.Model):
    action = models.ForeignKey('Action', verbose_name=u"Action", related_name="intentions")
    intention = models.CharField(u"Todays Intention", max_length=1000, help_text='What will you do today to bring you closer to your goal?')
    intended_metric = models.FloatField(u"Intended Metric", help_text='How much/many times will you perform the action?')
    enjoyable_aspects = models.CharField(u"What do you enjoy about this activity?", max_length=1000)
    created_date = models.DateTimeField(u"Date Created", auto_now_add=True)
    updated_date = models.DateTimeField(u"Date Updated", auto_now=True)

    def save(self, **kwargs):
        super(Intention, self).save(**kwargs)
        # self.project_intentionalignment()

    # def project_intentionalignment(self): # TODO  08/06/2019 18:01: Thsi should be a repo method
    #     intentionalignment_query = IntentionAlignmentProjection.objects.filter(goal=self.goal, intention=self)
    #     if intentionalignment_query.exists():
    #         intentionalignment_projection = intentionalignment_query.first()
    #         intentionalignment_projection.intention_metric = self.intended_metric
    #     else:
    #         intentionalignment_projection = IntentionAlignmentProjection(
    #             goal=self.goal,
    #             intention=self,
    #             measurement=None,
    #             intention_metric=self.intended_metric,
    #             measurement_metric=0
    #         )
    #     intentionalignment_projection.save()

    # def project_progress(self):
    #     all_progressprojections = ProgressProjection.objects.all()
    #     if all_progressprojections.exists():
    #         # cumulative sum of preceding intention metrics, plus current
    #         progress_intention_metric = sum([intention.intended_metric for intention in Intention.objects.all()]) + self.intended_metric
    #
    #     existing_progressprojection_query = ProgressProjection.objects.filter(goal=self.goal, intention=self)
    #     if existing_progressprojection_query.exists():
    #         progress_projection = existing_progressprojection_query.first()
    #         progress_projection.intention_metric = progress_intention_metric
    #     else:
    #         progress_projection = ProgressProjection(
    #             goal=self.goal,
    #             intention=self,
    #             measurement=None,
    #             intention_metric=progress_intention_metric,
    #             measurement_metric=0
    #         )
    #     progress_projection.save()

    class Meta:
        verbose_name = u"Intention"
        verbose_name_plural = u"Intentions"
        ordering = ("created_date", "action",)

    def __unicode__(self):
        return u"%s" % (self.createdate)
