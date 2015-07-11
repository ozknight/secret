from django.conf.urls import url
from .views import UpdateAccount


urlpatterns = [
    url(r'^(?P<pk>\d+)$', UpdateAccount.as_view(), name='update'),
]
