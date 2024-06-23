from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout as auth_logout
from .forms import LoginForm, RegistrationForm, TeacherForm, StudentForm, UserProfileForm, \
    TeacherProfileForm, StudentProfileForm
from .models import Teacher, Student, CustomUser


def register_view(request):
    user_form = RegistrationForm(request.POST or None)
    teacher_form = TeacherForm(request.POST or None)
    student_form = StudentForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid() and teacher_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            teacher = teacher_form.save(commit=False)
            student = student_form.save(commit=False)
            teacher.user = user
            student.user = user
            teacher.save()
            student.save()
            return redirect('accounts:login')
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
    return redirect('accounts:login')


@login_required
def profile_view(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if user.is_teacher:
        profile = get_object_or_404(Teacher, user=user)
    elif user.is_student:
        profile = get_object_or_404(Student, user=user)
    else:
        profile = None

    return render(request, 'accounts/profile.html', {'user': user, 'profile': profile})


@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)
        if user.is_teacher:
            profile_form = TeacherProfileForm(request.POST, request.FILES, instance=user.teacher)
        elif user.is_student:
            profile_form = StudentProfileForm(request.POST, request.FILES, instance=user.student)
        else:
            profile_form = None

        if user_form.is_valid() and (profile_form is None or profile_form.is_valid()):
            user_form.save()
            if profile_form:
                profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('accounts:profile', username=user.username)
    else:
        user_form = UserProfileForm(instance=user)
        if user.is_teacher:
            profile_form = TeacherProfileForm(instance=user.teacher)
        elif user.is_student:
            profile_form = StudentProfileForm(instance=user.student)
        else:
            profile_form = None

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

