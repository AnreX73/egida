from django.contrib import admin

from core.models import Specialization, Doctor, Schedule


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True


class ScheduleAdmin(admin.TabularInline):
    model = Schedule
    fields = ("day", "start_appointment", "end_appointment")
    save_on_top = True


class DoctorAdmin(admin.ModelAdmin):
    inlines = [ScheduleAdmin]
    list_display = (
        "id",
        "firstname",
        "fathername",
        "lastname",
        "speciality",
        "duration",
    )
    list_display_links = ("id", "firstname")
    prepopulated_fields = {"slug": ("lastname", "firstname")}
    save_on_top = True


admin.site.register(Doctor, DoctorAdmin)

admin.site.site_header = "Регистратура"
