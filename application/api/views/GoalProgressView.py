#!/usr/bin/env python2
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from domain.achievement.services.reporting.goal_progress.GoalProgressDataProvider import GoalProgressDataProvider
from application.api.serializers.GoalProgressSerializer import GoalProgressSerializer


class GoalProgressViewSet(ViewSet):
    serializer_class = GoalProgressSerializer

    def list(self, request):
        goal_progress_provider = GoalProgressDataProvider()
        goal_progress = goal_progress_provider.get_all_progress()
        serializer = GoalProgressSerializer(
            instance=goal_progress, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # goal_id = request.query_params.get('id')
        goal_progress_provider = GoalProgressDataProvider()
        goal_progress = goal_progress_provider.get_progress_for_goal(pk)
        serializer = GoalProgressSerializer(
            instance=goal_progress, many=True)
        return Response(serializer.data)

