from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^inflect$', views.inflect, name='inflect'),
]