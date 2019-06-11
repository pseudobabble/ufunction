#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Intention import Intention


class IntentionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intention
        fields = [
            'id',
            'action',
            'intention_text',
            'intended_metric',
            'enjoyable_aspects',
            'created_date',
            'updated_date',
        ]
