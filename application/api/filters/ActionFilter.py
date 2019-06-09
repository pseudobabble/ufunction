#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Action import Action


class ActionFilter(FilterSet):
    class Meta:
        model = Action
        fields = [
            'goal',
            'action_name',
            'target_metric',
            'target_metric_unit',
            'created_date',
            'updated_date'
        ]
