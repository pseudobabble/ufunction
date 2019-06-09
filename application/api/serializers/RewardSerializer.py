#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Reward import Reward


class RewardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reward
        fields = [
            'id',
            'goal',
            'reward_title',
            'reward_description',
            'achievement_metric',
            'obtained',
            'created_date',
            'updated_date'
        ]
