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

schedule_days = [1, 2, 5, 6]
now_month_cal = calendar.Calendar().monthdatescalendar(NOW.year, NOW.month)


def current_month_cal(year, month):
    return calendar.Calendar().monthdatescalendar(year, month)


def end_of_day(days):
    end_day = NOW + datetime.timedelta(days=days)
    return end_day

c = end_of_day(50)
print (c.month)
check_cal = current_month_cal(2024, 7)


def actual_calendar(current_month_cal, month=NOW.month):
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


all_actual_cal = actual_calendar(check_cal, 7)

print(all_actual_cal)


def week_schedule(schedule):
    schedule_days = [
        next((s for s in schedule if s.day == day), None) for day in standart_week
    ]
    return schedule_days
