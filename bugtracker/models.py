# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Statuses"


class Project(models.Model):
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, )
    project = models.ForeignKey(Project, )
    user = models.ForeignKey(User, )

    def __unicode__(self):
        return self.title



