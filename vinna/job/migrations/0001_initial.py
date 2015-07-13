# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150713_0211'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('essay', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('requirement', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'Posted')),
                ('due', models.DateTimeField(verbose_name=b'Due Date')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Hiring',
                'verbose_name_plural': 'Hirings',
            },
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Job Title')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job Category',
                'verbose_name_plural': 'Job Categories',
            },
        ),
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color_legend', models.CharField(max_length=10, verbose_name=b'Legend Color')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job Experience',
                'verbose_name_plural': 'Job Experiences',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Profession',
                'verbose_name_plural': 'Professions',
            },
        ),
        migrations.AddField(
            model_name='hiring',
            name='category',
            field=models.ForeignKey(to='job.JobCategory'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='company',
            field=models.ForeignKey(to='company.Company'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='job_experience_required',
            field=models.ForeignKey(to='job.JobExperience'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='job_type',
            field=models.ForeignKey(default=None, blank=True, to='job.JobType'),
        ),
        migrations.AddField(
            model_name='hiring',
            name='profession',
            field=models.ForeignKey(default=None, blank=True, to='job.Profession'),
        ),
        migrations.AddField(
            model_name='application',
            name='hiringform',
            field=models.ForeignKey(to='job.Hiring'),
        ),
        migrations.AddField(
            model_name='application',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
