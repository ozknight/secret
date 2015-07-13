from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):

    """Company model for Users who are Employeed"""

    owner = models.ForeignKey(User)
    logo = models.ImageField(upload_to='images/companyhumbs/')
    name = models.CharField(verbose_name='Name', max_length=100)
    address = models.CharField(verbose_name='Address', max_length=255)
    country = models.CharField(verbose_name='Country', max_length=100)
    province = models.CharField(verbose_name='Province', max_length=100)
    postal_code = models.SmallIntegerField(
        verbose_name='Postal Code', default=6000)
    email = models.EmailField(verbose_name='Email',)
    website = models.URLField(
        verbose_name='Website', blank=True)
    contact_person = models.CharField(
        verbose_name='Contact Person', max_length=255)
    timestamp = models.DateTimeField('Created', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyApprovalStatus(models.Model):
    company = models.OneToOneField(Company)
    status = models.BooleanField(default=False)
