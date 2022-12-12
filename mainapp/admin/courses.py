from django.contrib import admin

# Register your models here.

from mainapp.models import Courses
from django.utils.translation import gettext_lazy as _


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass
