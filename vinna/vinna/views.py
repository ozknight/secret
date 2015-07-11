from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic


class HomepageView(generic.TemplateView):

    """The Homepage Of Vinna"""

    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
            'page_title': 'Welcome To Vinna!',
        }
        if request.user and request.user.is_authenticated():
            context = {
                'page_title': 'Welcome ' +
                str(request.user.get_full_name() or request.user.username),
            }
            if not request.user.profile.is_Profile_Set():
                print 'profile not set'
                return HttpResponseRedirect(
                    reverse('profile:update', args=(request.user.id,))
                )
        return render(request, self.template_name, context)
