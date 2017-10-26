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
from job_search.models import Job_Post
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Job_Post.objects.all().order_by("-date")[:25],
                                template_name="job_search/job_search.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Job_Post, template_name = 'job_search/job_post.html')),
    url(r'^unfiltered/$', views.job_search_unfiltered, name = "job_search_unfiltered" ),
    url(r'^informationsystems_major/$', views.job_search_informationsystems_major, name = "job_search_informationsystem_major" ),
    url(r'^computerscience_major/$', views.job_search_computerscience_major, name = "job_search_computerscience_major" ),
    url(r'^computationalandsimsci_major/$', views.job_search_computationalandsimsci_major, name = "job_search_computationalandsimsci_major" ),
    url(r'^technologyinnovationanddesign_major/$', views.job_search_technologyinnovationanddesign_major, name = "job_search_technologyinnovationanddesign_major" ),
    url(r'^bpm/$', views.job_search_bpm, name = "job_search_bpm" ),
    url(r'^computationalandsimsci/$', views.job_search_computationalandsimsci_minor, name = "job_search_computationalandsimsci_minor" ),
    url(r'^computerscience_minor/$', views.job_search_computerscience_minor, name = "job_search_computerscience_minor" ),
    url(r'^datacentriccomputingextension/$', views.job_search_datacentriccomputingextension, name = "job_search_datacentriccomputingextension" ),
    url(r'^enterprisesystems/$', views.job_search_enterprisesystems, name = "job_search_enterprisesystems" ),
    url(r'^intelligentsystems/$', views.job_search_intelligentsystems, name = "job_search_intelligentsystems" ),
    url(r'^mobileapps/$', views.job_search_mobileapps, name = "job_search_mobileapps" ),
    url(r'^networkandsecurity/$', views.job_search_networkandsecurity, name = "job_search_networkandsecurity" ),
    url(r'^softwaredevelopmentforis/$', views.job_search_softwaredevelopmentforis, name = "job_search_softwaredevelopmentforis" ),
    url(r'^technologyinnovation/$', views.job_search_technologyinnovation, name = "job_search_technologyinnovation" ),
    url(r'^userexperience/$', views.job_search_userexperience, name = "job_search_userexperience" ),
    url(r'^analysis_skill/$', views.job_search_analysis_skill, name = "job_search_analysis_skill" ),
    url(r'^artificialintelligence_skill/$', views.job_search_artificialintelligence_skill, name = "job_search_artificialintelligence_skill" ),
    url(r'^cloudcomputing_skill/$', views.job_search_cloudcomputing_skill, name = "job_search_cloudcomputing_skill" ),
    url(r'^database_skill/$', views.job_search_database_skill, name = "job_search_database_skill" ),
    url(r'^design_skill/$', views.job_search_design_skill, name = "job_search_design_skill" ),
    url(r'^enterprisearchitecture_skill/$', views.job_search_enterprisearchitecture_skill, name = "job_search_enterprisearchitecture_skill" ),
    url(r'^gamesdevelopment_skill/$', views.job_search_gamedevelopment_skill, name = "job_search_gamedevelopment_skill" ),
    url(r'^hardware_skill/$', views.job_search_hardware_skill, name = "job_search_hardware_skill" ),
    url(r'^itconsulting_skill/$', views.job_search_itconsulting_skill, name = "job_search_itconsulting_skill" ),
    url(r'^itfundamentals_skill/$', views.job_search_itfundamentals_skill, name = "job_search_itfundamentals_skill" ),
    url(r'^modelling_skill/$', views.job_search_modelling_skill, name = "job_search_modelling_skill" ),
    url(r'^networking_skill/$', views.job_search_networking_skill, name = "job_search_networking_skill" ),
    url(r'^programming_skill/$', views.job_search_programming_skill, name = "job_search_programming_skill" ),
    url(r'^projectmanagement_skill/$', views.job_search_projectmanagement_skill, name = "job_search_projectmanagement_skill" ),
    url(r'^security_skill/$', views.job_search_security_skill, name = "job_search_security_skill" ),
    url(r'^socialmedia_skill/$', views.job_search_socialmedia_skill, name = "job_search_socialmedia_skill" ),
    url(r'^systemadministration_skill/$', views.job_search_systemadministration_skill, name = "job_search_systemadministration_skill" ),
    url(r'^webdevelopment_skill/$', views.job_search_webdevelopment_skill, name = "job_search_webdevelopment_skill" ),
]
