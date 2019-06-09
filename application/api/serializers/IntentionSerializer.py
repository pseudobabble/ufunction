#!/usr/bin/env python2

from rest_framework import serializers

from application.api.serializers.MeasurementSerializer import MeasurementSerializer
from domain.achievement.models.Goal.Intention import Intention


class IntentionSerializer(serializers.HyperlinkedModelSerializer):
    measurements = MeasurementSerializer(many=True, required=False)

    class Meta:
        model = Intention
        fields = [
            'id',
            'action',
            'intention',
            'intended_metric',
            'enjoyable_aspects',
            'created_date',
            'updated_date',
            'measurements'
        ]
