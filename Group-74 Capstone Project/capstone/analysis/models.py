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

class Chart(models.Model):
	name = models.CharField(max_length=50, db_column="Name")

class Line_Chart(models.Model):
	code = models.ForeignKey(Chart, on_delete=models.CASCADE)
	line_title = models.CharField(max_length=140) 
	january = models.IntegerField()
	february = models.IntegerField()
	march = models.IntegerField()
	april = models.IntegerField()
	may = models.IntegerField()
	june = models.IntegerField()
	july = models.IntegerField()
	august = models.IntegerField()
	september = models.IntegerField()
	october = models.IntegerField()
	november = models.IntegerField()
	december = models.IntegerField()

	def __unicode__(self):
		return self.line_title

class Pie_Chart(models.Model):
	code = models.ForeignKey(Chart, on_delete=models.CASCADE)
	pie_title = models.CharField(max_length=140) 
	information_system = models.IntegerField()
	combination = models.IntegerField()
	analysis = models.IntegerField()
	management = models.IntegerField()
	enterprise_architecture = models.IntegerField()
	consulting = models.IntegerField()
	project_management = models.IntegerField()
	sales = models.IntegerField()
	teachers = models.IntegerField()
	hardware_specialist = models.IntegerField()
	it_support = models.IntegerField()
	programming= models.IntegerField()
	testers= models.IntegerField()
	web_development= models.IntegerField()
	database= models.IntegerField()
	design = models.IntegerField()
	games = models.IntegerField()
	internship = models.IntegerField()
	networking  = models.IntegerField()
	security = models.IntegerField()
	system_administration = models.IntegerField()
	cloud = models.IntegerField()

	def __unicode__(self):
		return self.pie_title

class Bar_Chart(models.Model):
	code = models.ForeignKey(Chart, on_delete=models.CASCADE)
	bar_title = models.CharField(max_length=140) 
	analysis  = models.IntegerField()
	cIOManagement = models.IntegerField()
	database = models.IntegerField()
	design = models.IntegerField()
	enterpriseArchitecture = models.IntegerField()
	games = models.IntegerField()
	hardwareSpecialist = models.IntegerField()
	internshipWorkExp = models.IntegerField()
	consulting = models.IntegerField()
	itSupport = models.IntegerField()
	networking = models.IntegerField()
	programming = models.IntegerField()
	projectManagement = models.IntegerField()
	sales = models.IntegerField()
	security = models.IntegerField()
	systemAdministration = models.IntegerField()
	teachersTrainers = models.IntegerField()
	testers = models.IntegerField()
	virtualisationCloud = models.IntegerField()
	webDevelopment = models.IntegerField()

	def __unicode__(self):
		return self.bar_title