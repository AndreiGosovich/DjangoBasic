from django.contrib import admin

# Register your models here.

from mainapp.models import News
from django.utils.translation import gettext_lazy as _


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	search_fields = ["title", "preambule", "body"]

