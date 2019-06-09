#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Goal.Goal import Goal


class GoalFilter(FilterSet):
    class Meta:
        model = Goal
        fields = [
            'title',
            'end_state_description',
            'target_date',
            'complete',
            'created_date',
            'updated_date'
        ]
