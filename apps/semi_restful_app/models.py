from __future__ import unicode_literals
from django.db import models


class Validator(models.Manager):

    def valid_meth(self, data):
        errors = {}

        if len(data['title']) == 0:
            errors['name'] = "Title is a required field!"
        elif len(data['title']) < 2:
            errors['name'] = "Title should be atleast 2 characters!"

        if len(data['network']) == 0:
            errors['network'] = "Network is a required field!"
        elif len(data['network']) < 3:
            errors['network'] = "Network field requires atleast 3 characters!"

        if  data['desc'] and len(data['desc']) < 10:
            errors['desc'] = "Description field expects atleast 10 characters!"

        return errors



class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()






