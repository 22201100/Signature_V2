from students.models import Student
from attendance.models import Session, AttendanceRecord
def global_counts(request):
    try:
        return {
            'count_students': Student.objects.count(),
            'count_sessions': Session.objects.count(),
            'count_records': AttendanceRecord.objects.count()
        }
    except Exception:
        return {}
