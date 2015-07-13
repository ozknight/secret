from django import forms
from .models import Company


class CompanyCreationForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ('owner', 'contact_person')
