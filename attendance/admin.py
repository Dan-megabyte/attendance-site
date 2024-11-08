from django.contrib import admin

from .models import School, Club, Student

# Register your models here.

admin.site.register(School)
admin.site.register(Club)
admin.site.register(Student)