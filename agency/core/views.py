from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Doctor, Schedule
import datetime
import calendar
from core.schedule import end_of_day, standart_week, NOW, now_month_cal, standart_year
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
    end_day = end_of_day(doctor.pre_entry_days)
    cal = now_month_cal
    actual_schedule = [
        next((s for s in schedule if s.day == day), None) for day in standart_week
    ]
    mont_of_end_day = end_day.month
    months_quantity = mont_of_end_day - NOW.month + 1
    actual_cal = [
        [
            (
                day.day
                if day.month == NOW.month and day.weekday() in schedule_days
                else 0 if day.month == NOW.month else ''
            )
            for day in weeks
        ]
        for weeks in cal
    ]

    now_month = (standart_year[NOW.month])

    context = {
        "doctor": doctor,
        "schedule": actual_schedule,
        "standart_week": standart_week,
        "cal": actual_cal,
        "now": NOW,
        'now_month': now_month,
    }
    return render(request, "core/doctor_profile.html", context=context)
