from django import forms
from .models import Course, Session
class CourseForm(forms.ModelForm):
    class Meta: model = Course; fields = ['code','title','lecturer']
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session; fields = ['course','date','start_time','end_time','is_open']
        widgets = {'date': forms.DateInput(attrs={'type':'date'}),
                   'start_time': forms.TimeInput(attrs={'type':'time'}),
                   'end_time': forms.TimeInput(attrs={'type':'time'})}
