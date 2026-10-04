from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import SignUpForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        pform = ProfileForm(request.POST)
        if form.is_valid() and pform.is_valid():
            user = form.save()  # handles password hashing, validation, password2
            prof = user.profile
            for f,v in pform.cleaned_data.items():
                setattr(prof, f, v)
            prof.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = SignUpForm()
        pform = ProfileForm()
    return render(request, 'accounts/signup.html', {'form': form, 'pform': pform})

@login_required
def profile(request):
    prof = request.user.profile
    if request.method == 'POST':
        pform = ProfileForm(request.POST, instance=prof)
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')
        messages.error(request, 'Please correct the errors.')
    else:
        pform = ProfileForm(instance=prof)
    return render(request, 'accounts/profile.html', {'pform': pform})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Password changed!')
            return redirect('dashboard')
        messages.error(request, 'Fix errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
