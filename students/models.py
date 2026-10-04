from django.db import models

class Student(models.Model):
    student_id=models.CharField(max_length=30, unique=True)
    name=models.CharField(max_length=150)
    department=models.CharField(max_length=120, blank=True)
    email=models.EmailField(blank=True)
    photo=models.CharField(max_length=200, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.student_id} - {self.name}"

class FingerprintTemplate(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='templates')
    template_id=models.CharField(max_length=60)
    quality=models.IntegerField(default=0)
    captured_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.student} • {self.template_id}"
