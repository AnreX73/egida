import datetime

# from dateutil.rrule import rruleset, rrule, WEEKLY
# from dateutil.relativedelta import *
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

schedule_days = [0, 1, 5, 6]
now_month_cal = calendar.Calendar().monthdatescalendar(NOW.year, NOW.month)


def current_month_cal(year, month):
    return calendar.Calendar().monthdatescalendar(year, month)


def end_of_day(days):
    end_day = NOW + datetime.timedelta(days=days)
    return end_day


def actual_calendar(current_month_cal, month):
    actual_cal = [
        [
            (
                day
                if day.month == month and day.weekday() in schedule_days
                else 0 if day.month == month else ""
            )
            for day in weeks
        ]
        for weeks in current_month_cal
    ]
    return actual_cal


all_actual_cal = []  # all_actual_cal = actual_calendar(check_cal, 7)


def all_actual_calendar(days):
    month = NOW.month
    year = NOW.year
    while month <= end_of_day(days).month:
        # all_actual_cal.append(month)
        all_actual_cal.append(actual_calendar(current_month_cal(year, month), month))
        month += 1
    return all_actual_cal


# cal20 = all_actual_calendar(23)
# print(cal20)
# print('_______________________________________________________________________')


def week_schedule(schedule):
    schedule_days = [
        next((s for s in schedule if s.day == day), None) for day in standart_week
    ]
    return schedule_days
