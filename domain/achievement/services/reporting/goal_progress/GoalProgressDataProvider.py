#!/usr/bin/env python2
from domain.achievement.models.Goal import Goal
from domain.achievement.services.reporting.goal_progress.ProgressPoint import ProgressPoint


class GoalProgressDataProvider:

    def get_all_progress(self, accumulator, parent_goal=None):
        goals = Goal.objects.all()
        return goals
