from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Doctor, Schedule
import datetime
from dateutil.rrule import rruleset, rrule, WEEKLY
from dateutil.relativedelta import *
import calendar
from core.schedule import end_of_day, standart_week, NOW, now_month_cal







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
    actual_schedule = list(
        rrule(
            WEEKLY,
            byweekday=tuple(schedule_days),
            dtstart=(NOW),
            until=(end_day),
        )
    )
    cal = now_month_cal

    actual_cal = []
    for weeks in cal:
        actual_week = []
        for day in weeks:
            if day.day< NOW.day:
                actual_week.append(50)
            elif day.month != NOW.month:
                actual_week.append(50)
            elif day.weekday() in schedule_days and day.month == NOW.month:
                actual_week.append(day.day)
            else:
                actual_week.append(0)

        actual_cal.append(actual_week)

    context = {
        "doctor": doctor,
        "actual_schedule": actual_schedule,
        "now": NOW,
        "schedule": schedule,
        "standart_week": standart_week.values(),
        "cal": actual_cal,
        # 'cal1': cal1
    }
    return render(request, "core/doctor_profile.html", context=context)
