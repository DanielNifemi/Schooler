from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet

from accounts.models import CustomUser
from schooler import settings


class NoteManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


class AssignmentManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


class EventManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NoteManager()

    def clean(self):
        if not self.title:
            raise ValidationError("Title is required.")
        if len(self.title) > 100:
            raise ValidationError("Title cannot exceed 100 characters.")

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AssignmentManager()

    def clean(self):
        if not self.title:
            raise ValidationError("Title is required.")
        if len(self.title) > 100:
            raise ValidationError("Title cannot exceed 100 characters.")
        if not self.due_date:
            raise ValidationError("Due date is required.")

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()

    def __str__(self):
        return self.title

# TODO make sure to update them and add new models 'maybe'
