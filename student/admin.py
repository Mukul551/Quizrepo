from django.contrib import admin
from student.models import Student
# Register your models here.
class student(admin.ModelAdmin):
    list_display = ('user','profile_pic','address','mobile')

admin.site.register(Student,student)