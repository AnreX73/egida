from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from core.models import Doctor, Schedule
import datetime
from dateutil.rrule import rruleset, rrule, WEEKLY
from dateutil.relativedelta import *
import calendar


NOW = datetime.datetime.now()

standart_week = {
    0: "ПН",
    1: "ВТ",
    2: "СР",
    3: "ЧТ",
    4: "ПТ",
    5: "СБ",
    6: "ВС",
}


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
    schedule_days = Schedule.objects.filter(doctor_id=doctor.pk).values_list(
        "day", flat=True
    )
    end_day = NOW + datetime.timedelta(days=doctor.pre_entry_days)
    actual_schedule = list(
        rrule(
            WEEKLY,
            byweekday=tuple(schedule_days),
            dtstart=(NOW),
            until=(end_day),
        )
    )
    cal = calendar.Calendar().monthdatescalendar(NOW.year, NOW.month)
    # weekday_cal = [i.weekday for i in cal ]
    actual_cal = []
    for i in cal:
        for j in i:
            print(j.weekday())

    # print(schedule_days)
    # print(cal)
    context = {
        "doctor": doctor,
        "actual_schedule": actual_schedule,
        "now": NOW,
        "schedule": schedule,
        "standart_week": standart_week.values(),
        "cal": cal,
        # 'cal1': cal1
    }
    return render(request, "core/doctor_profile.html", context=context)
