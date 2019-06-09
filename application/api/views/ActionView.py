#!/usr/bin/env python2
import django_filters
from rest_framework import viewsets, generics

from application.api.serializers.ActionSerializer import ActionSerializer
from domain.achievement.models.Goal.Action import Action


class ActionViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Rewards to be viewed or edited.
    """
    serializer_class = ActionSerializer

    queryset = Action.objects.all()

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


