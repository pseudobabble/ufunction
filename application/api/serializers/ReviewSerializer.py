#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Review import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
