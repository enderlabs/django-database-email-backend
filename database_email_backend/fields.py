# -*- coding: utf-8 -*-
import base64
from django.db import models


# Stolen from http://djangosnippets.org/snippets/1669/
class Base64Field(models.TextField):

    def contribute_to_class(self, cls, name):
        if self.db_column is None:
            self.db_column = name
        self.field_name = name
        super(Base64Field, self).contribute_to_class(cls, self.field_name)
        setattr(cls, name, property(self.get_data, self.set_data))

    def get_data(self, obj):
        return base64.decodebytes(getattr(obj, self.field_name).encode('utf-8'))

    def set_data(self, obj, data):
        if data is not None:
            setattr(obj, self.field_name, base64.encodebytes(data).decode('utf-8'))
