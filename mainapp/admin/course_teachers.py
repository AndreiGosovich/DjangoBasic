from django.contrib import admin

# Register your models here.

from mainapp.models import CourseTeachers
from django.utils.translation import gettext_lazy as _


@admin.register(CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    pass
