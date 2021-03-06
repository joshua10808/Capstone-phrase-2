# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-16 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar_Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_title', models.CharField(max_length=140)),
                ('analysis', models.IntegerField()),
                ('cIOManagement', models.IntegerField()),
                ('database', models.IntegerField()),
                ('design', models.IntegerField()),
                ('enterpriseArchitecture', models.IntegerField()),
                ('games', models.IntegerField()),
                ('hardwareSpecialist', models.IntegerField()),
                ('internshipWorkExp', models.IntegerField()),
                ('consulting', models.IntegerField()),
                ('itSupport', models.IntegerField()),
                ('networking', models.IntegerField()),
                ('programming', models.IntegerField()),
                ('projectManagement', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('security', models.IntegerField()),
                ('systemAdministration', models.IntegerField()),
                ('teachersTrainers', models.IntegerField()),
                ('testers', models.IntegerField()),
                ('virtualisationCloud', models.IntegerField()),
                ('webDevelopment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Line_Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_title', models.CharField(max_length=140)),
                ('january', models.IntegerField()),
                ('february', models.IntegerField()),
                ('march', models.IntegerField()),
                ('april', models.IntegerField()),
                ('may', models.IntegerField()),
                ('june', models.IntegerField()),
                ('july', models.IntegerField()),
                ('august', models.IntegerField()),
                ('september', models.IntegerField()),
                ('october', models.IntegerField()),
                ('november', models.IntegerField()),
                ('december', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Pie_Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pie_title', models.CharField(max_length=140)),
                ('information_system', models.IntegerField()),
                ('combination', models.IntegerField()),
                ('analysis', models.IntegerField()),
                ('management', models.IntegerField()),
                ('enterprise_architecture', models.IntegerField()),
                ('consulting', models.IntegerField()),
                ('project_management', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('teachers', models.IntegerField()),
                ('hardware_specialist', models.IntegerField()),
                ('it_support', models.IntegerField()),
                ('programming', models.IntegerField()),
                ('testers', models.IntegerField()),
                ('web_development', models.IntegerField()),
                ('database', models.IntegerField()),
                ('design', models.IntegerField()),
                ('games', models.IntegerField()),
                ('internship', models.IntegerField()),
                ('networking', models.IntegerField()),
                ('security', models.IntegerField()),
                ('system_administration', models.IntegerField()),
                ('cloud', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Chart')),
            ],
        ),
        migrations.AddField(
            model_name='bar_chart',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.Chart'),
        ),
    ]
