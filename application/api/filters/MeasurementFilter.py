#!/usr/bin/env python2

from django_filters.rest_framework import FilterSet

from domain.achievement.models.Goal.Measurement import Measurement


class MeasurementFilter(FilterSet):
    class Meta:
        model = Measurement
        fields = [
            'action',
            'intention',
            'outcome_metric',
            'enjoyable_aspects',
            'difficult_aspects',
            'overcoming_difficult_aspects',
            'created_date',
            'updated_date'
        ]
