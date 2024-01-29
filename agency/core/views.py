from django.shortcuts import render

from core.models import Doctor


def index(request):
    context = {
        'title': 'главная страница'

    }
    return render(request, 'core/index.html', context=context)


def schedule(request):

    context = {
        'doctors': Doctor.objects.all()

               }
    return render(request, 'core/schedule.html', context=context)
