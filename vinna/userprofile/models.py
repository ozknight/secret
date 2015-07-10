from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)
MIN_VALID_AGE = 15
Valid_Gender = []
for Gender in GENDER:
    Valid_Gender.append(Gender[0])
    Valid_Gender.sort()


class Profile(models.Model):

    """User Profile Model"""
    user = models.OneToOneField(User)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER, blank=True)
    phone = models.CharField(
        'Contact #:', max_length=16, blank=True)
    about_you = models.TextField('About You :', blank=True)
    employer = models.BooleanField(default=False, blank=True)

    def is_employer(self):
        return self.employer

    def is_Profile_Set(self):
        if self.is_gender_valid and self.is_valid_user_age() and self.about_you:
            return True
        return False

    def is_valid_user_age(self):
        if not self.birthdate:
            return False
        age = timezone.now().year - self.birthdate.year
        return age >= MIN_VALID_AGE

    def is_gender_valid(self):
        if self.gender in Valid_Gender:
            return True
        return False

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    is_employer.boolean = True
    models.signals.post_save.connect(create_user_profile, sender=User)
