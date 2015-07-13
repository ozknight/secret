from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from vinna.settings import MEDIA_URL

from company.models import Company


class HomepageView(generic.TemplateView):

    """The Homepage Of Vinna"""

    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        try:
            profile = Company.objects.filter(owner=request.user)
        except Exception:
            profile = False

        context = {
            'user': request.user,
            'page_title': 'Welcome To Vinna!',
        }
        if request.user and request.user.is_authenticated():
            context = {
                'page_title': 'Welcome ' +
                str(request.user.get_full_name() or request.user.username),
                'media': MEDIA_URL
            }
            if not request.user.profile.is_Profile_Set():
                print 'profile not set'
                return HttpResponseRedirect(
                    reverse('profile:update', args=(request.user.id,))
                )
        return render(request, self.template_name, context)
