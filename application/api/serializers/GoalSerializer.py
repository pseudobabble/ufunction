#!/usr/bin/env python2

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from domain.achievement.models.Goal import Goal


class GoalSerializer(serializers.ModelSerializer):
    subgoals = RecursiveField(many=True, required=False)  # Generates nested json result from one->many relationship

    class Meta:
        model = Goal
        fields = [
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
            'is_parent',
            'num_title_chars',
            'title_truncated',
            'subgoals'
        ]
        read_only_fields = ['subgoals']  # Prevents framework from requiring subgoals on create/update

