from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Worker(models.Model):
    """
    holds the worker model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Task(models.Model):
    """
    holds the task model
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    target_date = models.DateTimeField(blank=False, null=False)
    worker = models.ForeignKey(Worker, related_name='tasks', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
