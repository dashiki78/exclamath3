from django.contrib import admin
from .models import Student, Course, DailyNote
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('level', 'middle_unit', 'small_unit', 'index',)


@admin.register(DailyNote)
class DailyNoteAdmin(admin.ModelAdmin):
    list_display=('name', 'study_day',)
