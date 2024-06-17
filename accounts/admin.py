from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Teacher, Student


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture', 'is_teacher', 'is_student')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
