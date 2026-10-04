from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from attendance.models import AttendanceRecord
from django.db.models.functions import TruncDate
from django.db.models import Count

@login_required
def index(request):
    return render(request, 'reports/index.html')

@login_required
def attendance_json(request):
    data = AttendanceRecord.objects.annotate(d=TruncDate('created_at')).values('d').annotate(n=Count('id')).order_by('d')
    labels=[str(x['d']) for x in data]
    counts=[x['n'] for x in data]
    return JsonResponse({'labels': labels, 'counts': counts})
