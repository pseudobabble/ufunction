#!/usr/bin/env python2
from django_filters.rest_framework import FilterSet

from domain.achievement.models.Reward import Reward


class RewardFilter(FilterSet):
    class Meta:
        model = Reward
        fields = [
            'goal',
            'reward_title',
            'reward_description',
            'achievement_metric',
            'obtained',
            'created_date',
            'updated_date'
        ]
