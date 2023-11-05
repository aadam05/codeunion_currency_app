from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CronExecutionLogAdmin(admin.ModelAdmin):
  list_display = ('name', 'rate')
  list_filter = ('name', 'rate')
