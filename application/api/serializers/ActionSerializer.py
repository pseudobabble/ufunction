#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Action import Action
from custom_fields.ChoicesField import ChoicesField


class ActionSerializer(serializers.ModelSerializer):
    action_verb = ChoicesField(choices=Action.ACTION_VERBS)

    class Meta:
        model = Action
        fields = (
            'id',
            'goal',
            'action_verb',
            'activity',
            'target_metric',
            'target_metric_unit',
            'created_date',
            'updated_date',
        )
