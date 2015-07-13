from django import forms
from models import *


class CreateHiringForm(forms.ModelForm):

    """Form For Creating A New Hiring(s)"""

    class Meta:
        model = Hiring
        exclude = ('company', 'status',)
