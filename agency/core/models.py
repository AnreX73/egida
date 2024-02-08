from django.db import models
from django.urls import reverse


class Specialization(models.Model):
    name = models.CharField(max_length=20, verbose_name="Специальность")
    slug = models.SlugField(
        unique=True, max_length=100, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
        ordering = ["id"]


class Doctor(models.Model):
    firstname = models.CharField(max_length=250, verbose_name="Имя доктора")
    fathername = models.CharField(max_length=250, verbose_name="Отчество доктора")
    lastname = models.CharField(max_length=250, verbose_name="Фамилия доктора")
    slug = models.SlugField(
        unique=True, max_length=100, db_index=True, verbose_name="URL"
    )

    speciality = models.ForeignKey(
        Specialization,
        default=1,
        verbose_name="специальность",
        on_delete=models.CASCADE,
        related_name="doctor_spec",
    )
    duration = models.IntegerField(
        verbose_name="продолжительность приема в минутах (с запасом 5 минут)"
    )

    pre_entry_days = models.IntegerField(
        default=14, verbose_name="предварительная запись на прием (кол-во дней)"
    )

    def __str__(self):
        return self.lastname

    def get_absolute_url(self):
        return reverse("doctor_profile", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"
        ordering = ["id"]


class Schedule(models.Model):
    class WeekDays(models.IntegerChoices):
        MONDAY = 0, "Понедельник"
        TUESDAY = 1, "Вторник"
        WEDNESDAY = 2, "Среда"
        THURSDAY = 3, "Четверг"
        FRIDAY = 4, "Пятница"
        SATURDAY = 5, "Суббота"
        SUNDAY = 6, "Воскресенье"

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="doctor_schedule",
        verbose_name="расписание",
    )
    day = models.SmallIntegerField(choices=WeekDays.choices, verbose_name="День недели")

    start_appointment = models.IntegerField(verbose_name="Начало приема", default=7)
    end_appointment = models.SmallIntegerField(
        verbose_name="Окончание приема", default=24
    )

    class Meta:
        verbose_name = "Приемный день"
        verbose_name_plural = "Приемные дни"
        ordering = ["id"]
