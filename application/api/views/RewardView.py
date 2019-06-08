#!/usr/bin/env python2

from rest_framework import viewsets

from application.api.serializers.RewardSerializer import RewardSerializer
from domain.achievement.services.GoalRepository import GoalRepository


class RewardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Rewards to be viewed or edited.
    """
    goals = GoalRepository.get_all()

    serializer_class = RewardSerializer
