from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name','last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role','phone','department']
