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

    def save(self, **kwargs):
        super(Measurement, self).save(**kwargs)
        # self.project_intentionalignment()
        # self.project_progress()

    # def project_intentionalignment(self): # TODO  08/06/2019 18:04: these should be repo methods
    #     intentionalignment_query = IntentionAlignmentProjection.objects.filter(goal=self.goal, intention=self.intention)
    #     if intentionalignment_query.exists():
    #         intentionalignment_projection = intentionalignment_query.first()
    #         intentionalignment_projection.measurement = self
    #         intentionalignment_projection.measurement_metric = self.outcome_metric
    #     else:
    #         intentionalignment_projection = IntentionAlignmentProjection(
    #             goal=self.goal,
    #             intention=self.intention,
    #             measurement=self,
    #             intention_metric=self.intention.intended_metric,
    #             measurement_metric=self.outcome_metric
    #         )
    #     intentionalignment_projection.save()
    #
    # def project_progress(self):
    #     for progress_projection in ProgressProjection.objects.filter(goal_id=self.goal_id):
    #         progress_projection.delete()
    #
    #     progress_dataprovider = ProgressDataProvider(self.goal_id)
    #     progress_data = progress_dataprovider.get_progress_data()
    #     for item in progress_data:
    #         item['goal_id'] = self.goal_id
    #         item['measurement_id'] = self.id
    #         item['intention_id'] = self.intention. id
    #         progress_projection = ProgressProjection(**item)
    #         progress_projection.save()



    class Meta:
        verbose_name = u"Measurement"
        verbose_name_plural = u"Measurements"
        ordering = ("created_date", "action",)

    def __unicode__(self):
        return u"%s" % (self.createdate)
