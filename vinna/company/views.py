from django.contrib import messages
from django.views import generic
from .models import Company
from .forms import CompanyCreationForm
# Create your views here.


class CreateCompanyView(generic.CreateView):

    """View for Creating A Company"""

    model = Company
    form_class = CompanyCreationForm
    success_url = '/'
    template_name = 'Company_Creation.html'

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyView, self).get_context_data(**kwargs)
        context['page_title'] = "Create A Company"
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        form.instance.owner = request.user
        form.instance.contact_person = request.user.username

        if form.is_valid():
            messages.add_message(
                request, messages.INFO,
                'You\'ve Successfully Created Your Company!')
            return self.form_valid(form)
        else:
            messages.add_message(
                request, messages.ERROR, 'Something Went Wrong!')
            return self.form_invalid(form)
