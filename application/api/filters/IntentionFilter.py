#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Intention import Intention


class IntentionFilter(FilterSet):
    class Meta:
        model = Intention
        fields = [
            'action',
            'intention',
            'intended_metric',
            'enjoyable_aspects',
            'created_date',
            'updated_date'
        ]
