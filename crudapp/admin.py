# myapp/admin.py
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'age')
    search_fields = ('Name',)

admin.site.register(Student, StudentAdmin)
