#!/usr/bin/env python2

from rest_framework import serializers

from application.api.serializers.IntentionSerializer import IntentionSerializer
from domain.achievement.models.Goal.Action import Action


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    intentions = IntentionSerializer(many=True, required=False)

    class Meta:
        model = Action
        fields = (
            '__all__'
        )
