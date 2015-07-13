from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^new$', CreateCompanyView.as_view(), name='create'),
]
