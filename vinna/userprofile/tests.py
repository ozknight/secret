import datetime
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile
# Create your tests here.

Fiftheen_Year = datetime.timedelta(days=365) * 15


def Setup_User():
    user = User(username='test')
    user.save()
    return user


class UserProfile_TestCase(TestCase):

    def test_for_age_below_standard(self):
        """Test For Underage Users"""
        user = Setup_User()
        profile = Profile(user=user, birthdate=datetime.date.today())
        self.assertEquals(profile.is_valid_user_age(), False)

    def test_for_age_equals_standard(self):
        """Test For Users With Valid Age Level"""
        user = Setup_User()
        age = datetime.date.today() - Fiftheen_Year
        profile = Profile(user=user, birthdate=age)
        self.assertEquals(profile.is_valid_user_age(), True)

    def test_for_age_above_standard(self):
        """Test For Users With Above Valid Age Level"""
        user = Setup_User()
        age = datetime.date.today() - (Fiftheen_Year * 2)
        profile = Profile(user=user, birthdate=age)
        self.assertEquals(profile.is_valid_user_age(), True)

    def test_for_no_age(self):
        """Test For Users With No Age"""
        user = Setup_User()
        profile = Profile(user=user)
        self.assertEquals(profile.is_valid_user_age(), False)

    def test_for_male_user(self):
        """Test for Male Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='M')
        self.assertEquals(profile.is_gender_valid(), True)

    def test_for_female_user(self):
        """Test for Female Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='F')
        self.assertEquals(profile.is_gender_valid(), True)

    def test_for_not_valid_gender_user(self):
        """Test for Female Users"""
        user = Setup_User()
        profile = Profile(user=user, gender='D')
        self.assertEquals(profile.is_gender_valid(), False)

    def test_for_no_gender_user(self):
        """Test for Female Users"""
        user = Setup_User()
        profile = Profile(user=user)
        self.assertEquals(profile.is_gender_valid(), False)
