from django.contrib import admin

# Register your models here.

from mainapp.models import Lesson
from django.utils.translation import gettext_lazy as _


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ["id", "get_course_name", "num", "title", "deleted"]
	ordering = ["-course__name", "-num"]
	list_per_page = 5
	list_filter = ["course", "created", "deleted"]
	actions = ["mark_deleted"]

	def get_course_name(self, obj):
		return obj.course.name

	def mark_deleted(self, request, queryset):
		count = queryset.update(deleted=True)
		message = _(
			"Delete lessons, %(count)d" % {
				'count': count
			}
		)

	mark_deleted.short_description = _("Mark deleted")

	get_course_name.short_description = _("Course")