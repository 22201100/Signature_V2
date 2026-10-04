from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='reports_index'),
    path('attendance.json', views.attendance_json, name='reports_attendance_json')
]