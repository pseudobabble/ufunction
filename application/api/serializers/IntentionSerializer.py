#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Intention import Intention


class IntentionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intention
        fields = '__all__'
