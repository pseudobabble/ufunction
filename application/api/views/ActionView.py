#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from application.api.filters.ActionFilter import ActionFilter
from application.api.serializers.ActionSerializer import ActionSerializer
from domain.achievement.models.Goal.Action import Action


class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Actions to be viewed or edited.
    """
    serializer_class = ActionSerializer

    queryset = Action.objects.all()

    filter_backends = [DjangoFilterBackend]
    filter_class = ActionFilter
