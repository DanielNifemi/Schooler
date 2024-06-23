from calendar import HTMLCalendar
from datetime import datetime, timedelta

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Assignment, Event, Note


@login_required
def note_list(request):
    try:
        notes = Note.objects.filter(user=request.user)

        search_query = request.GET.get('search')
        if search_query:
            notes = notes.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        status_filter = request.GET.get('status')
        if status_filter:
            notes = notes.filter(status=status_filter)

        context = {
            'notes': notes,
        }
        return render(request, 'school/note_list.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('home')


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'school/note_detail.html', {'note': note})


@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        note = Note.objects.create(title=title, description=description, user=request.user)
        return redirect('school:note_detail', pk=note.pk)
    return render(request, 'school/note_form.html')


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.description = request.POST['description']
        note.save()
        return redirect('school:note_detail', pk=note.pk)
    return render(request, 'school/note_form.html', {'note': note})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('school:notes')
    return render(request, 'school/note_confirm_delete.html', {'note': note})


@login_required
def assignment_list(request):
    try:
        assignments = Assignment.objects.filter(user=request.user)

        search_query = request.GET.get('search')
        if search_query:
            assignments = assignments.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        status_filter = request.GET.get('status')
        if status_filter:
            assignments = assignments.filter(status=status_filter)

        priority_filter = request.GET.get('priority')
        if priority_filter:
            assignments = assignments.filter(priority=priority_filter)

        context = {
            'assignments': assignments,
        }
        return render(request, 'school/assignment_list.html', context)
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('home')


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    return render(request, 'school/assignment_detail.html', {'assignment': assignment})


@login_required
def assignment_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        assignment = Assignment.objects.create(title=title, description=description, due_date=due_date,
                                               user=request.user)
        return redirect('school:assignment_detail', pk=assignment.pk)
    return render(request, 'school/assignment_form.html')


@login_required
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == 'POST':
        assignment.title = request.POST['title']
        assignment.description = request.POST['description']
        assignment.due_date = request.POST['due_date']
        assignment.save()
        return redirect('school:assignment_detail', pk=assignment.pk)
    return render(request, 'school/assignment_form.html', {'assignment': assignment})


@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    if request.method == 'POST':
        assignment.delete()
        return redirect('school:assignments')
    return render(request, 'school/assignment_confirm_delete.html', {'assignment': assignment})


@login_required
def calendar_view(request):
    today = datetime.now().date()
    prev_month = today - timedelta(days=32)
    prev_month = prev_month.replace(day=1)
    next_month = today.replace(day=28) + timedelta(days=4)
    next_month = next_month.replace(day=1)

    events = Event.objects.filter(user=request.user, date__gte=prev_month, date__lt=next_month)

    cal = HTMLCalendar()
    calendar_html = cal.formatmonth(today.year, today.month)

    context = {
        'calendar_html': calendar_html,
        'events': events,
        'today': today,
        'prev_month': prev_month,
        'next_month': next_month,
    }

    return render(request, 'school/calendar.html', context)


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('school:events')
    else:
        form = EventForm()
    return render(request, 'school/event_form.html', {'form': form})


@login_required
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('school:events')
    else:
        form = EventForm(instance=event)
    return render(request, 'school/event_form.html', {'form': form})

@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('school:events')
    return render(request, 'school/event_confirm_delete.html', {'event': event})

@login_required
def events_view(request):
    events = Event.objects.filter(user=request.user)
    context = {
        'events': events,
    }
    return render(request, 'school/events.html', context)
