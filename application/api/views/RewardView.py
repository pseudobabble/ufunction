#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from application.api.filters.RewardFilter import RewardFilter
from application.api.serializers.RewardSerializer import RewardSerializer
from domain.achievement.models.Reward import Reward


class RewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rewards to be viewed or edited.
    """
    queryset = Reward.objects.all()

    serializer_class = RewardSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = RewardFilter
