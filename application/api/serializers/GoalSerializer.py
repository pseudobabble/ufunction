#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal import Goal
from application.api.serializers.ActionSerializer import ActionSerializer


class GoalSerializer(serializers.HyperlinkedModelSerializer):
    actions = ActionSerializer(many=True, required=False)

    class Meta:
        model = Goal
        fields = (
            'id',
            'title',
            'end_state_description',
            'target_date',
            'complete',
            'created_date',
            'updated_date',
            'actions'
        )
