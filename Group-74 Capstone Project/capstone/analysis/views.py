# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponse
from .models import Line_Chart


def index(request):
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
	return render(request, 'analysis/analysis.html', context)


# Create your views here.


