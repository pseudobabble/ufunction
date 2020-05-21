#!/usr/bin/env python2
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

class ObjectSerializer(serializers.BaseSerializer):
    """
    A read-only serializer that coerces arbitrary complex objects
    into primitive representations.
    """
    def to_representation(self, instance):
        output = {}
        for attribute_name in dir(instance):
            attribute = getattr(instance, attribute_name)
            if attribute_name.startswith('_'):
                # Ignore private attributes.
                pass
            elif hasattr(attribute, '__call__'):
                # Ignore methods and other callables.
                pass
            elif isinstance(attribute, (str, int, bool, float, type(None))):
                # Primitive types can be passed through unmodified.
                output[attribute_name] = attribute
            elif isinstance(attribute, list):
                # Recursively deal with items in lists.
                output[attribute_name] = [
                    self.to_representation(item) for item in attribute
                ]
            elif isinstance(attribute, dict):
                # Recursively deal with items in dictionaries.
                output[attribute_name] = {
                    str(key): self.to_representation(value)
                    for key, value in attribute.items()
                }
            else:
                # Force anything else to its string representation.
                output[attribute_name] = str(attribute)
        return output

class GoalProgressSerializer(serializers.Serializer):
    parent_goal = serializers.IntegerField()
    verb = serializers.CharField()
    verb_phrase = serializers.CharField()
    target_date = serializers.DateField()
    end_state_description = serializers.CharField()
    urgency = serializers.FloatField()
    importance = serializers.FloatField()
    complete = serializers.BooleanField()
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()
    title = serializers.CharField()
    eisenhower_score = serializers.FloatField()
    is_parent = serializers.BooleanField()
    # subgoals = serializers.ListField(child=RecursiveField(), required=False)

    # def to_representation(self, instance):
    #     output = {}
    #     print instance.__dict__
    #     for attribute_name in dir(instance):
    #         attribute = getattr(instance, attribute_name)
    #         if attribute_name.startswith('_'):
    #             # Ignore private attributes.
    #             pass
    #         elif hasattr(attribute, '__call__'):
    #             # Ignore methods and other callables.
    #             pass
    #         elif isinstance(attribute, (str, int, bool, float, type(None))):
    #             # Primitive types can be passed through unmodified.
    #             output[attribute_name] = attribute
    #         elif isinstance(attribute, list):
    #             # Recursively deal with items in lists.
    #             output[attribute_name] = [
    #                 self.to_representation(item) for item in attribute
    #             ]
    #         elif isinstance(attribute, dict):
    #             # Recursively deal with items in dictionaries.
    #             output[attribute_name] = {
    #                 str(key): self.to_representation(value)
    #                 for key, value in attribute.items()
    #             }
    #         else:
    #             # Force anything else to its string representation.
    #             output[attribute_name] = str(attribute)
    #     return output
