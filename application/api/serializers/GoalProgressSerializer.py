#!/usr/bin/env python2

from rest_framework import serializers


class GoalProgressSerializer(serializers.Serializer):
    target_metric = serializers.FloatField()
    outcome_metric = serializers.FloatField()
    goal_id = serializers.IntegerField()
    action_id = serializers.IntegerField()
    measurement_id = serializers.IntegerField()
