from django.contrib import admin
from .models import *


class MYAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data', 'time')
    list_filter = ('name', 'data')
    search_fields = ('name', 'data')




admin.site.register(Activity, MYAdmin)
