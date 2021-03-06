#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Measurement import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            'id',
            'action',
            'intention',
            'outcome_metric',
            'enjoyable_aspects',
            'difficult_aspects',
            'overcoming_difficult_aspects',
            'created_date',
            'updated_date'
        ]
