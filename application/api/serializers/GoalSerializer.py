#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal import Goal


class GoalSerializer(serializers.ModelSerializer):
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
        )
