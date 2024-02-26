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

standart_year = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}

now_month_cal = calendar.Calendar().monthdatescalendar(NOW.year, NOW.month)


def week_schedule(schedule):
    schedule_days = [
        next((s for s in schedule if s.day == day), None) for day in standart_week
    ]


def end_of_day(days):
    end_day = NOW + datetime.timedelta(days=days)
    return end_day


def actual_calendar(end_day):
    actual_cal = [
        [
            (
                day
                if day.month == NOW.month and day.weekday() in schedule_days
                else 0 if day.month == NOW.month else ""
            )
            for day in weeks
        ]
        for weeks in now_month_cal
    ]
    return actual_cal
