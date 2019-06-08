#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Action import Action


class ActionSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Action
        fields = (
            'goal',
            'action_name',
            'target_metric',
            'target_metric_unit',
            'created_date',
            'updated_date',
        )
