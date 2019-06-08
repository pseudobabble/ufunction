#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Reward import Reward


class RewardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'
