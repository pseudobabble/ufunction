#!/usr/bin/env python2


class ProgressPoint:

    def __init__(
            self,
            action_target_metric,
            measurement_outcome_metric,
            goal_id,
            action_id,
            measurement_id
    ):
        self.goal_id = goal_id
        self.action_id = action_id
        self.measurement_id = measurement_id
        self.outcome_metric = measurement_outcome_metric
        self.target_metric = action_target_metric

    def get_target_metric(self):
        return self.target_metric

    def get_outcome_metric(self):
        return self.outcome_metric

    def get_goal_id(self):
        return self.goal_id

    def get_action_id(self):
        return self.action_id

    def get_measurement_id(self):
        return self.measurement_id
