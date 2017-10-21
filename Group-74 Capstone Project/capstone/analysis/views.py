# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Chart
from .models import Line_Chart
from .models import Pie_Chart
from .models import Bar_Chart

# Create your views here.

def index(request):

	lineChartA = Line_Chart.objects.get(id = 1);
	lineChartB = Line_Chart.objects.get(id = 2);
	lineChartC = Line_Chart.objects.get(id = 3);
	lineChartD = Line_Chart.objects.get(id = 4);
	pieChartA = Pie_Chart.objects.get(id = 1);
	barChartA = Bar_Chart.objects.get(id = 1);

	context = {
        'lineChartA': lineChartA,
        'lineChartB': lineChartB,
        'lineChartC': lineChartC,
        'lineChartD': lineChartD,

        'pieChartA' : pieChartA,
        'barChartA' : barChartA,
        }
	return render(request, 'analysis/analysis.html', context)

def line(request):

	lineChartA = Line_Chart.objects.get(id = 1);
	lineChartB = Line_Chart.objects.get(id = 2);
	lineChartC = Line_Chart.objects.get(id = 3);
	lineChartD = Line_Chart.objects.get(id = 4);

	context = {
        'lineChartA': lineChartA,
        'lineChartB': lineChartB,
        'lineChartC': lineChartC,
        'lineChartD': lineChartD,
        }
	return render(request, 'analysis/ITJobs.html', context)

def pie(request):

	pieChartA = Pie_Chart.objects.get(id = 1);

	context = {
       'pieChartA' : pieChartA,
        }
	return render(request, 'analysis/JobsMajorBreakdown.html', context)

def bar(request):

	barChartA = Bar_Chart.objects.get(id = 1);

	context = {
        'barChartA' : barChartA,
        }
	return render(request, 'analysis/SkillsDemand.html', context)



