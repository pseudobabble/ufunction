#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Goal import Goal
from application.api.serializers.ActionSerializer import ActionSerializer


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    actions = ActionSerializer(many=True, required=False)

    class Meta:
        model = Goal
        fields = (
            '__all__'
        )
