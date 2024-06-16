from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from .forms import LoginForm, RegistrationForm, TeacherForm, StudentForm
from .models import Teacher, Student


def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user_form.cleaned_data['is_teacher']:
                teacher_form = TeacherForm(request.POST)
                if teacher_form.is_valid():
                    teacher = teacher_form.save(commit=False)
                    teacher.user = user
                    teacher.save()
            elif user_form.cleaned_data['is_student']:
                student_form = StudentForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        user_form = RegistrationForm()
        teacher_form = TeacherForm()
        student_form = StudentForm()

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'teacher_form': teacher_form,
        'student_form': student_form
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def home(request):
    return render(request, 'school/home.html')
