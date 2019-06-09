#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from application.api.filters.MeasurementFilter import MeasurementFilter
from application.api.serializers.MeasurementSerializer import MeasurementSerializer
from domain.achievement.models.Measurement import Measurement


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Measurements to be viewed or edited.
    """
    serializer_class = MeasurementSerializer

    queryset = Measurement.objects.all()

    filter_backends = [DjangoFilterBackend]
    filter_class = MeasurementFilter
