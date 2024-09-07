from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseName', 'courseSkill', 'courseDateTime')
    search_fields = ('courseName', 'courseSkill')
    list_filter = ('courseDateTime',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'approved')
    search_fields = ('studentID', 'approved')
    list_filter = ('approved',)
