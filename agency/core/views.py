from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Doctor, Schedule
import datetime
import calendar
from core.schedule import (
    standart_week,
    NOW,
)


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
    schedule_days_list = Schedule.objects.filter(doctor_id=doctor.pk).values_list(
        "day", flat=True
    )
    schedule_days = [
        next((s for s in schedule if s.day == day), None) for day in standart_week
    ]

    end_of_pre_entry = NOW + datetime.timedelta(days=doctor.pre_entry_days)

    def current_month_cal(year, month):
        return calendar.Calendar().monthdatescalendar(year, month)

    def actual_calendar(current_month_cal, month):
        actual_cal = [
            [
                (
                    day
                    if day.month == month and day.weekday() in schedule_days_list
                    else 0 if day.month == month else ""
                )
                for day in weeks
            ]
            for weeks in current_month_cal
        ]
        return actual_cal

    def all_actual_calendar(days):
        all_actual_cal = []
        month = NOW.month
        year = NOW.year
        while month <= end_of_pre_entry.month:
            # all_actual_cal.append(standart_year[month])
            all_actual_cal.append(actual_calendar(current_month_cal(year, month), month))
            month += 1
        return all_actual_cal

    actual_cal = all_actual_calendar(doctor.pre_entry_days)

    context = {
        "doctor": doctor,
        "schedule": schedule_days,
        "standart_week": standart_week,
        "cal": actual_cal,
        'end_day': end_of_pre_entry,
        'now': NOW

    }
    return render(request, "core/doctor_profile.html", context=context)
