from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from core.models import Doctor, Schedule
import datetime


def index(request):
    context = {"title": "главная страница"}
    return render(request, "core/index.html", context=context)


def schedule(request):
    doctors = Doctor.objects.all()

    context = {"doctors": doctors}

    return render(request, "core/schedule.html", context=context)


def doctor_profile(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    schedule = Schedule.objects.filter(doctor_id=doctor.pk)
    now = datetime.datetime.now()

    context = {
        "doctor": doctor,
        'schedule':schedule,
        'now':now
        }
    

    return render(request, "core/doctor_profile.html", context=context)
