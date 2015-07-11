from django.views import generic
from .models import Profile
# from .forms import ProfileUpdateForm
# Create your views here.


class UpdateAccount(generic.UpdateView):

    """Page where User Could Update There User Details"""

    template_name = 'Update_User_Profile_View.html'
    model = Profile
    fields = ['profile_image', 'birthdate',
              'gender', 'phone', 'about_you', 'employer']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateAccount, self).form_valid(form)
