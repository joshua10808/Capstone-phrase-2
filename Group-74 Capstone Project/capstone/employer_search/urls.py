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
from employer_search.models import Employer_Post
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Employer_Post.objects.all().order_by("-date")[:25],
                                template_name="employer_search/employer_search.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Employer_Post, template_name = 'employer_search/employer_post.html')),
    url(r'^unfiltered/$', views.employer_search_unfiltered, name = "employer_search_unfiltered"),
    url(r'^0/$', views.employer_search_a, name = "employer_search_0" ),
    url(r'^a/$', views.employer_search_a, name = "employer_search_a" ),
    url(r'^b/$', views.employer_search_a, name = "employer_search_b" ),
    url(r'^c/$', views.employer_search_a, name = "employer_search_c" ),
    url(r'^d/$', views.employer_search_a, name = "employer_search_d" ),
    url(r'^e/$', views.employer_search_a, name = "employer_search_e" ),
    url(r'^f/$', views.employer_search_a, name = "employer_search_f" ),
    url(r'^g/$', views.employer_search_a, name = "employer_search_g" ),
    url(r'^h/$', views.employer_search_a, name = "employer_search_h" ),
    url(r'^i/$', views.employer_search_a, name = "employer_search_i" ),
    url(r'^j/$', views.employer_search_a, name = "employer_search_j" ),
    url(r'^k/$', views.employer_search_a, name = "employer_search_k" ),
    url(r'^l/$', views.employer_search_a, name = "employer_search_l" ),
    url(r'^m/$', views.employer_search_a, name = "employer_search_m" ),
    url(r'^n/$', views.employer_search_a, name = "employer_search_n" ),
    url(r'^o/$', views.employer_search_a, name = "employer_search_o" ),
    url(r'^p/$', views.employer_search_a, name = "employer_search_p" ),
    url(r'^q/$', views.employer_search_a, name = "employer_search_q" ),
    url(r'^r/$', views.employer_search_a, name = "employer_search_r" ),
    url(r'^s/$', views.employer_search_a, name = "employer_search_s" ),
    url(r'^t/$', views.employer_search_a, name = "employer_search_t" ),
    url(r'^u/$', views.employer_search_a, name = "employer_search_u" ),
    url(r'^v/$', views.employer_search_a, name = "employer_search_v" ),
    url(r'^w/$', views.employer_search_a, name = "employer_search_w" ),
    url(r'^x/$', views.employer_search_a, name = "employer_search_x" ),
    url(r'^y/$', views.employer_search_a, name = "employer_search_y" ),
    url(r'^z/$', views.employer_search_a, name = "employer_search_z" ),
    
]
