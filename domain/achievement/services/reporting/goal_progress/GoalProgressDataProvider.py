#!/usr/bin/env python2

from domain.achievement.models.Goal import Goal
from domain.achievement.services.reporting.goal_progress.ProgressPoint import ProgressPoint


class GoalProgressDataProvider:

    def get_progress_for_goal(self, goal_id):
        progress = []
        if goal_id:
            goal = Goal.objects.get(id=goal_id)
            if goal:
                for action in goal.actions.all():
                    for measurement in action.measurements.all():
                        progress_point = ProgressPoint(action.target_metric, measurement.outcome_metric)
                        progress.append(progress_point)
        return progress

    def get_all_progress(self):
        progress = []
        goals = Goal.objects.all()
        for goal in goals:
            for action in goal.actions.all():
                for measurement in action.measurements.all():
                    progress_point = ProgressPoint(action.target_metric, measurement.outcome_metric)
                    progress.append(progress_point)
        return progress



