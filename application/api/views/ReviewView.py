#!/usr/bin/env python2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from application.api.filters.ReviewFilter import ReviewFilter
from application.api.serializers.ReviewSerializer import ReviewSerializer
from domain.achievement.models.Review import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Goals to be viewed or edited.
    """
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = ReviewFilter
