from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teacher, Student


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_teacher', 'is_student')}),
    )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'department', 'bio')
    search_fields = ('user__username', 'department')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'phone_number', 'major', 'bio')
    search_fields = ('user__username', 'grade', 'major')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
