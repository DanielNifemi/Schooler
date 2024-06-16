from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Teacher, Student


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    is_teacher = forms.BooleanField(label='Register as Teacher', required=False)
    is_student = forms.BooleanField(label='Register as Student', required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password', 'is_teacher', 'is_student']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['phone_number', 'department', 'bio']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['grade', 'phone_number', 'major', 'bio']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
