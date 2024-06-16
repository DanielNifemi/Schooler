from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment_detail'),
]
