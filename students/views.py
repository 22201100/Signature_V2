from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student, FingerprintTemplate
from .forms import StudentForm, TemplateForm

@login_required
def student_list(request):
    q = request.GET.get('q','').strip()
    qs = Student.objects.all().order_by('-created_at')
    if q:
        qs = qs.filter(name__icontains=q) | qs.filter(student_id__icontains=q)
    page = Paginator(qs, 12).get_page(request.GET.get('page'))
    return render(request, 'students/list.html', {'page': page, 'q': q})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Student registered.')
            return redirect('student_detail', pk=obj.id)
        messages.error(request, 'Please correct the errors.')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Register Student'})

@login_required
def student_detail(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'obj': obj})

@login_required
def student_update(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated.')
            return redirect('student_detail', pk=obj.id)
        messages.error(request, 'Please correct the errors.')
    else:
        form = StudentForm(instance=obj)
    return render(request, 'students/form.html', {'form': form, 'title': 'Update Student'})

@login_required
def student_delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Student deleted.')
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'obj': obj})

@login_required
def template_create(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Template saved.')
            return redirect('student_detail', pk=form.cleaned_data['student'].id)
        messages.error(request, 'Please correct the errors.')
    else:
        form = TemplateForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Fingerprint Template'})
