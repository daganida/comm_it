from django.conf.urls import url

from workey_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]