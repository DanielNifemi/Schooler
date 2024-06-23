from django.urls import path
from . import views

app_name = "school"

urlpatterns = [
    path('notes/', views.note_list, name='notes'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/create/', views.note_create, name='create_note'),
    path('notes/update/<int:pk>/', views.note_update, name='update_note'),
    path('notes/delete/<int:pk>/', views.note_delete, name='delete_note'),
    path('assignment-create/', views.assignment_create, name='create_assignment'),
    path('assignments/', views.assignment_list, name='assignments'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('assignment-update/<int:pk>/', views.assignment_update, name='update_assignment'),
    path('assignment-delete/<int:pk>/', views.assignment_delete, name='delete_assignment'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('events/', views.events_view, name='events'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:pk>/', views.update_event, name='update_event'),
    path('events/delete/<int:pk>/', views.delete_event, name='delete_event'),
]
