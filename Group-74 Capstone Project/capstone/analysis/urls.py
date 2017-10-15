"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from analysis.models import Analysis_Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Analysis_Post.objects.all().order_by("-date")[:25],
                                template_name="analysis/analysis.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Analysis_Post, template_name = 'analysis/analysis_post.html')),
    url(r'^ITJobs/$', ListView.as_view(queryset=Analysis_Post.objects.all(),template_name="analysis/ITJobs.html")),
    url(r'^JobsMajorBreakdown/$', ListView.as_view(queryset=Analysis_Post.objects.all(),template_name="analysis/JobsMajorBreakdown.html")),
    url(r'^SkillsDemand/$', ListView.as_view(queryset=Analysis_Post.objects.all(),template_name="analysis/SkillsDemand.html")),
]

