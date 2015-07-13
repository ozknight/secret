from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^create/$', CreateJobView.as_view(), name='create_hiring'),
]
