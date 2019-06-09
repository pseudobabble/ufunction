#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Review import Review


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = [
            'goal',
            'review_period',
            'review_period_start_date',
            'review_period_end_date',
            'enjoyable_aspects',
            'difficult_aspects',
            'overcome_difficult_aspects',
            'next_period_focus',
            'created_date',
            'updated_date'
        ]
