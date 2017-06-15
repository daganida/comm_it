from django.conf.urls import url

from workey_app import views

urlpatterns = [
    url(r'workers-tasks$', views.workers_tasks, name='workers_tasks'),
]