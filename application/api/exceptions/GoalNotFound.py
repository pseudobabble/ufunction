#!/usr/bin/env python2


class GoalNotFound(Exception):
    def __init__(self, goal_id):
        message = 'Goal with id {} was not found'.format(goal_id)

        # Call the base class constructor with the parameters it needs
        super(GoalNotFound, self).__init__(message)
