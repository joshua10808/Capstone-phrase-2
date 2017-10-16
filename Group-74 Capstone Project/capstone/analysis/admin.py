# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Chart
from .models import Line_Chart
from .models import Pie_Chart
from .models import Bar_Chart



myModels = [Chart, Line_Chart, Pie_Chart, Bar_Chart]

admin.site.register(myModels)


# Register your models here.
