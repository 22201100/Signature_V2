from django.db import models
from students.models import Student

class Course(models.Model):
    code=models.CharField(max_length=40, unique=True)
    title=models.CharField(max_length=200)
    lecturer=models.CharField(max_length=120, blank=True)
    def __str__(self): return f"{self.code} - {self.title}"

class Session(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sessions')
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    is_open=models.BooleanField(default=True)
    def __str__(self): return f"{self.course.code} • {self.date}"

class AttendanceRecord(models.Model):
    session=models.ForeignKey(Session, on_delete=models.CASCADE, related_name='records')
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    matched=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    source=models.CharField(max_length=30, default='fingerprint')
    def __str__(self): return f"{self.session} • {self.student}"
