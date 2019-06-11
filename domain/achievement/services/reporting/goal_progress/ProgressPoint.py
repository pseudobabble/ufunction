#!/usr/bin/env python2


class ProgressPoint:

    def __init__(self, action_target_metric, measurement_outcome_metric):
        self.outcome_metric = measurement_outcome_metric
        self.target_metric = action_target_metric

    def get_target_metric(self):
        return self.target_metric

    def get_outcome_metric(self):
        return self.outcome_metric
