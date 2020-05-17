#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from application.api.filters.GoalFilter import GoalFilter
from application.api.serializers.GoalSerializer import GoalSerializer
from domain.achievement.models.Goal import Goal


class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Goals to be viewed or edited.
    """
    queryset = Goal.objects.all()

    serializer_class = GoalSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    filter_class = GoalFilter
