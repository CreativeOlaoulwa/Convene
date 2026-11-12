from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Registration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone

def home(request):
    upcoming = Event.objects.filter(end_date__gte=timezone.now()).order_by('start_date')[:3]
    context = {
        'upcoming': upcoming,
        'event_count': Event.objects.count(),
        'registration_count': Registration.objects.count(),
    }
    return render(request, 'events/home.html', context)


def event_list(request):
    events = Event.objects.order_by('start_date')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    already_registered = Registration.objects.filter(event=event, attendee=request.user).exists()

    if already_registered:
        messages.info(request, "You're already registered for this event.")
    elif event.registrations.count() >= event.capacity:
        messages.error(request, "Sorry, this event is full.")
    else:
        Registration.objects.create(event=event, attendee=request.user)
        messages.success(request, f"You're registered for {event.title}!")

    return redirect('event_detail', pk=event.pk)



@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(attendee=request.user)
    return render(request, 'events/my_registrations.html', {'registrations': registrations})


@login_required
def cancel_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk, attendee=request.user)
    event_title = registration.event.title
    registration.delete()
    messages.success(request, f"Registration for {event_title} cancelled.")
    return redirect('my_registrations')


def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def event_checkin(request, pk):
    event = get_object_or_404(Event, pk=pk)
    registrations = Registration.objects.filter(event=event)

    if request.method == 'POST':
        reg_id = request.POST.get('registration_id')
        registration = get_object_or_404(Registration, pk=reg_id, event=event)
        registration.checked_in = True
        registration.checked_in_at = timezone.now()
        registration.save()
        messages.success(request, f"{registration.attendee.username} checked in.")
        return redirect('event_checkin', pk=event.pk)

    return render(request, 'events/event_checkin.html', {'event': event, 'registrations': registrations})