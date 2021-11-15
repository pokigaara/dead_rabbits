from django.contrib import admin
from .models import *


class MYAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data', 'time')


admin.site.register(Activity, MYAdmin)
