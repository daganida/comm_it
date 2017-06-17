from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from workey_app.models import Worker
from django.contrib.auth.decorators import login_required


def index(request):

    user = request.user
    context = {}
    if user is not AnonymousUser:
        context['user'] = user
    return render(request, 'workey/index.html', context)


@login_required(login_url='/login')
def workers_tasks(request):
    user = request.user
    context = {}
    if user is not AnonymousUser:
        worker = user.worker
        context['worker'] = worker
    return render(request, 'workey/workers_tasks.html', context)
