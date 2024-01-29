from django.contrib import admin

from core.models import DaysOfWeek, Specialization, Doctor, Schedule


# @admin.register(DaysOfWeek)
# class DaysOfWeekAdmin(admin.ModelAdmin):
#     pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ScheduleAdmin(admin.TabularInline):
    model = Schedule
    fields = ("day", "start_appointment", "end_appointment")



class DoctorAdmin(admin.ModelAdmin):
    inlines = [ScheduleAdmin]
    prepopulated_fields = {"slug": ("lastname", "firstname")}



admin.site.register(Doctor, DoctorAdmin)

admin.site.site_header = "Регистратура"
