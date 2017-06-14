from django.shortcuts import render

# Create your views here.
from workey_app.models import Worker


def index(request):
    workers_tasks = {}
    workers = Worker.objects.all()
    counter = 0
    for worker in workers:
        workers_tasks[worker] = worker.tasks.all()
    context = {'workers_tasks': workers_tasks, 'counter':counter}
    return render(request, 'workey/index.html', context)