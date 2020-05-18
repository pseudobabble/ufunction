#!/usr/bin/env python2
from domain.achievement.models.Goal import Goal
from domain.achievement.services.reporting.goal_progress.ProgressPoint import ProgressPoint


class GoalProgressDataProvider:

    def get_progress_for_goal(self, goal_id):
        progress = []
        if goal_id:
            goal = Goal.objects.get(id=goal_id)
            if goal:
                for subgoal in goal.subgoals.all():
                    for measurement in subgoal.measurements.all():
                        progress_point = ProgressPoint(
                            subgoal.target_metric,
                            measurement.outcome_metric,
                            goal.id,
                            subgoal.id,
                            measurement.id
                        )
                        progress.append(progress_point)
        return progress

    def get_all_progress(self):
        progress = []
        goals = Goal.objects.all()
        for goal in goals:
            pass

        return [
            {
                'name': 'Top Level',
                'attributes': {
                    'keyA': 'val A',
                    'keyB': 'val B',
                    'keyC': 'val C',
                },
                'children': [
                    {
                        'name': 'Level 2: A',
                        'attributes': {
                            'keyA': 'val A',
                            'keyB': 'val B',
                            'keyC': 'val C',
                        },
                        'children': [
                            {
                                'name': 'Level 2: A',
                                'attributes': {
                                    'keyA': 'val A',
                                    'keyB': 'val B',
                                    'keyC': 'val C',
                                },
                            },
                            {
                                'name': 'Level 2: B',
                                'attributes': {
                                    'keyA': 'val A',
                                    'keyB': 'val B',
                                    'keyC': 'val C',
                                },
                                'children': [
                                    {
                                        'name': 'Level 2: A',
                                        'attributes': {
                                            'keyA': 'val A',
                                            'keyB': 'val B',
                                            'keyC': 'val C',
                                        },
                                    },
                                    {
                                        'name': 'Level 2: B',
                                        'attributes': {
                                            'keyA': 'val A',
                                            'keyB': 'val B',
                                            'keyC': 'val C',
                                        },
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        'name': 'Level 2: B',
                        'attributes': {
                            'keyA': 'val A',
                            'keyB': 'val B',
                            'keyC': 'val C',
                        },
                    },
                ],
            },
        ]



