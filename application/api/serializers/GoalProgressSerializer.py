#!/usr/bin/env python2

from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

class GoalProgressSerializer(serializers.Serializer):
    name = serializers.CharField()
    attributes = serializers.DictField()
    children = serializers.ListField(child=RecursiveField(), required=False)
