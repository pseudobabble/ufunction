#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Measurement import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
