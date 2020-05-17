#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = (
            'id',
            'parent_goal',
            'title',
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
            # 'subgoals'
        )
