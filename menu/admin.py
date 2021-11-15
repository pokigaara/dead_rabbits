from django.contrib import admin
from .models import *


class MYAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'name', 'weight', 'price')


admin.site.register(Menu, MYAdmin)
admin.site.register(Categories)
