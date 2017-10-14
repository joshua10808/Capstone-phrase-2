# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Analysis_Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Line_Chart(models.Model):
	a_January = models.IntegerField()
	a_February = models.IntegerField()
	a_March = models.IntegerField()
	a_April = models.IntegerField()
	a_May = models.IntegerField()
	a_June = models.IntegerField()
	a_July = models.IntegerField()
	a_August = models.IntegerField()
	a_September = models.IntegerField()
	a_October = models.IntegerField()
	a_November = models.IntegerField()
	a_December = models.IntegerField()