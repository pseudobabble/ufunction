#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Goal import Goal


class GoalFilter(FilterSet):
    class Meta:
        model = Goal
        fields = [
            'stative_verb',
            'status',
            'target_date',
            'end_state_description',
            'complete',
            'created_date',
            'updated_date'
        ]
