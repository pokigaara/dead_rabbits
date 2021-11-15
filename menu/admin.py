from django.contrib import admin
from .models import *


class MYAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories', 'name', 'weight', 'price')
    list_filter = ('categories', 'name', 'weight', 'price')
    search_fields = ('name', 'price')


admin.site.register(Menu, MYAdmin)
admin.site.register(Categories)
