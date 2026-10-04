from django.urls import path
from . import views
urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('new/', views.device_create, name='device_create'),
    path('<int:pk>/edit/', views.device_update, name='device_update'),
    path('<int:pk>/delete/', views.device_delete, name='device_delete'),
    path('connect/', views.connect, name='device_connect'),
    path('logs/<int:pk>/', views.device_logs, name='device_logs'),
]
