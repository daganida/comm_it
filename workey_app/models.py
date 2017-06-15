from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.user.first_name + ' ' +self.user.last_name

    def __str__(self):
        return self.user.first_name + ' ' +self.user.last_name



class Task(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    target_date = models.DateTimeField(blank=False,null=False)
    worker = models.ForeignKey(Worker,related_name='tasks',on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name




