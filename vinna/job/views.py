from django.views import generic
from .models import *
from .forms import CreateHiringForm
# Create your views here.


class CreateJobView(generic.CreateView):
    form_class = CreateHiringForm
    template_name = 'Hiring_Create_View.html'
