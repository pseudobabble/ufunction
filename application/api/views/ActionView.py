#!/usr/bin/env python2
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response

from application.api.Exceptions.GoalNotFound import GoalNotFound
from application.api.serializers.ActionSerializer import ActionSerializer
from domain.achievement.services.GoalRepository import GoalRepository


class ActionViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Rewards to be viewed or edited.
    """
    serializer_class = ActionSerializer

    def list(self):
        goal_id = self._get_goal_id_or_fail()

        actions = None
        if goal_id:
            goal = GoalRepository.get_by_id(goal_id)
            actions = goal.actions

        if not actions:
            raise GoalNotFound(goal_id)

        actions_serializer = ActionSerializer(actions, many=True)

        return Response(actions_serializer.data)


    # def create(self):
    #     goal_id = self._get_goal_id_or_fail('goal_id')
    #
    #     goal = GoalRepository.get_by_id(goal_id)
    #     if goal:
    #
    #
    #
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
        pass

    def _get_goal_id_or_fail(self):
        goal_id = self.request.query_params.get('goal_id')
        if not goal_id:
            goal_id = 'None'
            raise GoalNotFound(goal_id)
        return goal_id
