from django.conf.urls import url

from workey_app import views

urlpatterns = [
    url(r'^$', views.workers, name='workers'),
]