from django.urls import path
from .views import about, settings_view
urlpatterns=[
    path('about/', about, name='about'),
    path('settings/', settings_view, name='settings_view'),
]