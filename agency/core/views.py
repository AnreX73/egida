from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Doctor, Schedule
import datetime
import calendar
from core.schedule import (
    standart_week,
    NOW,
    now_month_cal,
    standart_year,
    week_schedule,
)
from dateutil import relativedelta


def index(request):
    context = {"title": "главная страница"}
    return render(request, "core/index.html", context=context)


@login_required(login_url="/")
def schedule(request):
    doctors = Doctor.objects.all()

    context = {"doctors": doctors}

    return render(request, "core/schedule.html", context=context)


@login_required(login_url="/")
def doctor_profile(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    schedule = Schedule.objects.filter(doctor_id=doctor.pk)
    schedule_days = Schedule.objects.filter(doctor_id=doctor.pk).values_list(
        "day", flat=True
    )

    cal = now_month_cal
    actual_schedule = week_schedule(schedule)
    actual_cal = [
        [
            (
                day
                if day.month == NOW.month and day.weekday() in schedule_days
                else 0 if day.month == NOW.month else ""
            )
            for day in weeks
        ]
        for weeks in cal
    ]
    end_day = end_of_day(doctor.pre_entry_days)
    now_month = standart_year[NOW.month]
    print(end_day.month) 
    context = {
        "doctor": doctor,
        "schedule": actual_schedule,
        "standart_week": standart_week,
        "cal": actual_cal,
        "now": NOW,
        "now_month": now_month,
    }
    return render(request, "core/doctor_profile.html", context=context)
