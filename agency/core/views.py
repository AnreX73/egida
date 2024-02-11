from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from core.models import Doctor, Schedule
import datetime
from dateutil.rrule import *
from dateutil.relativedelta import *


NOW = datetime.datetime.now()


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
    schedule_days = Schedule.objects.filter(doctor_id=doctor.pk).values_list('day', flat=True)
    end_day = NOW + datetime.timedelta(days=doctor.pre_entry_days)
    actual_schedule = list(
        rrule(
            WEEKLY,
            byweekday=tuple(schedule_days),
            dtstart=(NOW),
            until=(end_day),
        )
    )
   
    context = {
        "doctor": doctor,
        "actual_schedule": actual_schedule,
        "now": NOW,
        'schedule': schedule,
        
    }
    return render(request, "core/doctor_profile.html", context=context)
