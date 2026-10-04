from django import forms
from .models import Student, FingerprintTemplate

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id','name','department','email','photo']

class TemplateForm(forms.ModelForm):
    class Meta:
        model = FingerprintTemplate
        fields = ['student','template_id','quality']
