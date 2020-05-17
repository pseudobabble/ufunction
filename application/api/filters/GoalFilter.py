#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import NumberFilter

from django.db.models import F

from domain.achievement.models.Goal import Goal


class GoalFilter(FilterSet):
    eisenhower_score = NumberFilter(method='filter_eisenhower_score')

    class Meta:
        model = Goal
        fields = [
            'parent_goal',
            'verb',
            'verb_phrase',
            'target_date',
            'end_state_description',
            'urgency',
            'importance',
            'eisenhower_score',
            'complete',
            'created_date',
            'updated_date',
            'subgoals'
        ]

    # TODO note 17/05/2020 12:59: How to filter on a calculated field/virtual property (but it doesnt make a diff to the value on FE?)
    def filter_eisenhower_score(self, queryset, value):
        if value:
            queryset = queryset.annotate(eisenhower_score=((F('urgency') * F('importance'))/100)).filter(eisenhower_score=value)
        return queryset
