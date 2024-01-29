from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from core.models import Doctor, Schedule
import datetime


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
    end_day = NOW + datetime.timedelta(days=31)
    delta = end_day - NOW
    check_arr = []
    for i in range(delta.days):
        d = (NOW + datetime.timedelta(days=i))
        check_arr.append(d.date)

        
    print (check_arr)

   
   

    context = {
        "doctor": doctor,
        'schedule':schedule,
        'now':NOW,
        'check_arr': check_arr
        }
    

    return render(request, "core/doctor_profile.html", context=context)
