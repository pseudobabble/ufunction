#!/usr/bin/env python2

from rest_framework import viewsets

from application.api.serializers.GoalSerializer import GoalSerializer
from domain.achievement.services.GoalRepository import GoalRepository


class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Goals to be viewed or edited.
    """
    queryset = GoalRepository.get_all()

    serializer_class = GoalSerializer
