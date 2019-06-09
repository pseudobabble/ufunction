#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from application.api.filters.IntentionFilter import IntentionFilter
from application.api.serializers.IntentionSerializer import IntentionSerializer
from domain.achievement.models.Goal.Intention import Intention


class IntentionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Intentions to be viewed or edited.
    """
    serializer_class = IntentionSerializer

    queryset = Intention.objects.all()

    filter_backends = [DjangoFilterBackend]
    filter_class = IntentionFilter
