from django.contrib import admin
from .models import Course, Session, AttendanceRecord
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(AttendanceRecord)
