import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from company.models import Company
# Create your models here.


class JobCategory(models.Model):

    """Sets Of Job Categories For Hiring Classification Purposes"""

    name = models.CharField('Job Title', max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'


class JobExperience(models.Model):

    """Sets Of Job Experience For Hiring Classification Purposes"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    color_legend = models.CharField('Legend Color', max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Experience'
        verbose_name_plural = 'Job Experiences'


class JobType(models.Model):

    """Sets Of Job Type for Hiring Classification Purposes"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'


class Profession(models.Model):

    """Sets Of Job Type for Hiring Classification Purposes"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'


class Hiring(models.Model):

    """Serves As A Hiring Form Created By Companies"""

    company = models.ForeignKey(Company)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirement = models.TextField()
    timestamp = models.DateTimeField('Posted', auto_now_add=True)
    due = models.DateTimeField('Due Date')
    status = models.BooleanField(default=True)
    category = models.ForeignKey(JobCategory)
    job_experience_required = models.ForeignKey(JobExperience)
    job_type = models.ForeignKey(JobType, default=None, blank=True)
    profession = models.ForeignKey(
        Profession, default=None, blank=True)

    def __unicode__(self):
        return self.title + " by " + self.company.__str__()

    @property
    def valid_for_hiring(self):
        now = timezone.now() - datetime.timedelta(days=1)
        return now <= self.due

    class Meta:
        verbose_name = 'Hiring'
        verbose_name_plural = 'Hirings'


class Application(models.Model):

    """
    Serves as a form that a user has to obtain
    before applying to any given job advertisement
    """

    owner = models.ForeignKey(User)
    hiringform = models.ForeignKey(Hiring)
    essay = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.owner.__str__()

    def get_status(self):
        return self.status
    get_status.boolean = True
