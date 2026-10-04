from django.contrib import admin
from django.urls import path, include
from core.views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('attendance/', include('attendance.urls')),
    path('devices/', include('devices.urls')),
    path('reports/', include('reports.urls')),
    path('core/', include('core.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
