from django.contrib import admin
from reservation.models import *


class MyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date', 'time', 'table')
    list_filter = ('id', 'name', 'phone', 'date', 'time', 'table')
    search_fields = ('name', 'phone', 'time', 'table', 'date')


admin.site.register(Reserv, MyAdmin)
# Register your models here.
