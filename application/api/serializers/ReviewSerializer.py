#!/usr/bin/env python2

from rest_framework import serializers

from domain.achievement.models.Goal.Review import Review


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'goal',
            'review_period',
            'review_period_start',
            'review_period_end',
            'enjoyable_aspects',
            'difficult_aspects',
            'overcome_difficult_aspects',
            'next_period_focus',
            'created_date',
            'updated_date'
        ]
