# Joshua test progress


# -*- coding: utf-8 -*-

# import from mysql database *** 可能可以直接call class not create one
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Job_Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title
