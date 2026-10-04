from django.urls import path
from . import views
urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/new/', views.course_create, name='course_create'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/new/', views.session_create, name='session_create'),
    path('sessions/<int:pk>/edit/', views.session_update, name='session_update'),
    path('sessions/<int:pk>/delete/', views.session_delete, name='session_delete'),
    path('records/<int:session_id>/', views.session_records, name='session_records'),
    path('records/<int:session_id>/<int:record_id>/delete/', views.record_delete, name='record_delete'),
    path('export/csv/', views.export_csv, name='export_csv'),
]
