from django.urls import path
from . import views

app_name = "school"

urlpatterns = [
    path('notes/', views.note_list, name='notes'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('assignment-create/', views.assignment_create, name='create_assignment'),
    path('assignments/', views.assignment_list, name='assignments'),
    path('assignment-update/', views.assignment_update, name='update_assignment'),
    path('assignment-delete/', views.assignment_delete, name='delete_assignment'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('events/', views.events_view,  name='events'),
]
