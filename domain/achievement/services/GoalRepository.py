#!/usr/bin/env python2

from application.infrastructure.Repository import Repository

from domain.achievement.models.Goal.Goal import Goal


GoalRepository = Repository(Goal)

