from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Course, Session, AttendanceRecord
from .forms import CourseForm, SessionForm
from students.models import Student
import csv

# ---- Courses CRUD ----
@login_required
def course_list(request):
    items = Course.objects.all().order_by('code')
    return render(request, 'attendance/course_list.html', {'items': items})

@login_required
def course_create(request):
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created.')
            return redirect('course_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = CourseForm()
    return render(request, 'attendance/form.html', {'form': form, 'title': 'Create Course'})

@login_required
def course_update(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        form = CourseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated.')
            return redirect('course_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = CourseForm(instance=obj)
    return render(request, 'attendance/form.html', {'form': form, 'title': 'Update Course'})

@login_required
def course_delete(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        obj.delete()
        messages.success(request, 'Course deleted.')
        return redirect('course_list')
    return render(request, 'attendance/confirm_delete.html', {'obj': obj})

# ---- Sessions CRUD ----
@login_required
def session_list(request):
    items = Session.objects.select_related('course').order_by('-date','-start_time')
    return render(request, 'attendance/session_list.html', {'items': items})

@login_required
def session_create(request):
    if request.method=='POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Session created.')
            return redirect('session_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = SessionForm()
    return render(request, 'attendance/form.html', {'form': form, 'title': 'Create Session'})

@login_required
def session_update(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    if request.method=='POST':
        form = SessionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Session updated.')
            return redirect('session_list')
        messages.error(request, 'Fix errors below.')
    else:
        form = SessionForm(instance=obj)
    return render(request, 'attendance/form.html', {'form': form, 'title': 'Update Session'})

@login_required
def session_delete(request, pk):
    obj = get_object_or_404(Session, pk=pk)
    if request.method=='POST':
        obj.delete()
        messages.success(request, 'Session deleted.')
        return redirect('session_list')
    return render(request, 'attendance/confirm_delete.html', {'obj': obj})

# ---- Records ----
@login_required
def session_records(request, session_id):
    s = get_object_or_404(Session, pk=session_id)
    students = Student.objects.all().order_by('student_id')
    if request.method=='POST':
        sid = request.POST.get('student_id')
        matched = request.POST.get('matched') == 'on'
        st = get_object_or_404(Student, student_id=sid)
        AttendanceRecord.objects.create(session=s, student=st, matched=matched, source='manual')
        messages.success(request, 'Attendance added.')
        return redirect('session_records', session_id=s.id)
    recs = AttendanceRecord.objects.filter(session=s).select_related('student').order_by('-created_at')
    return render(request, 'attendance/records.html', {'session': s, 'records': recs, 'students': students})

@login_required
def record_delete(request, session_id, record_id):
    rec = get_object_or_404(AttendanceRecord, pk=record_id, session_id=session_id)
    rec.delete()
    messages.success(request, 'Record deleted.')
    return redirect('session_records', session_id=session_id)

# ---- Export CSV ----
@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=attendance.csv'
    writer = csv.writer(response)
    writer.writerow(['Session','Student ID','Student Name','Matched','Source','Time'])
    for r in AttendanceRecord.objects.select_related('session','student').order_by('-created_at'):
        writer.writerow([str(r.session), r.student.student_id, r.student.name, r.matched, r.source, r.created_at])
    return response
