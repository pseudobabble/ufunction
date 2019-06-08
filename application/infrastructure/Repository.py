#!/usr/bin/env python2


class Repository(object):
    def __init__(self, model):
        """

        :rtype:
        """
        self.model = model

    def get_all(self):
        """
        :return: QuerySet
        """
        return self.model.objects.all()

    def get_by_id(self, id):
        """

        :param id: integer
        :return: object
        """
        return self.model.objects.get(id=id)

    def get_by(self, field_name_query_value_dict):
        """
        Pass a dictionary like {field_name_1: query_value_1, field_name_2: query_value_2}
        :param kwargs: dict
        :return: QuerySet
        """
        return self.model.objects.filter(**field_name_query_value_dict)

    def save(self, model):
        """
        :param model: object
        """
        if not isinstance(model, self.model):
            raise TypeError(
                'Attempted to save a {} using the GoalRepository, please use the appropriate Repository instead'
            )
        model.save()
