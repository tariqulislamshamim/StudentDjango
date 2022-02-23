from django.contrib import admin
from .models import AbsentDate, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(AbsentDate)