from django.shortcuts import render, redirect, get_object_or_404
from app.models import Event, RegisteredEvents, CreatedEvents
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from app.forms import EventForm


# Create your views here.
def event_index(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'app/event_index.html', context)


def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    attendees = RegisteredEvents.objects.filter(event=event)
    context = {
        'event': event,
        'attendees': attendees
    }
    return render(request, 'app/event_detail.html', context)


def view_map(request, pk):
    event = Event.objects.get(pk=pk)
    context = {
        'event': event
    }
    if not event.location:
        return HttpResponseRedirect(reverse('app:event_detail', args={pk}))
    return render(request, 'app/map.html', context)


# def create_event(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('app:event_index'))
#     if request.method == "POST":
#         form = EventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('app:event_index'))
#     else:
#         form = EventForm()
#         context = {
#             'form': form,
#             'logged_in': True
#         }
#         return render(request, 'app/create_event.html', context)


def create_event(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    if request.method == "POST":
        title = request.POST['title']
        day = request.POST['date']
        if title == '' or day == "":
            context = {
                'failed': True
            }
            return render(request, 'app/create_event.html', context)
        info = request.POST['info']
        location = request.POST['location']
        image = request.FILES.get('image', False)

        event = Event.objects.create(title=title, day=day)
        if not info == '':
            event.info = info
        if not location == '':
            event.location = location
        if image:
            event.image = image
        event.poster = request.user.get_full_name()
        event.save()
        created_event = CreatedEvents(event=event, user=request.user)
        created_event.save()
        return HttpResponseRedirect(reverse('app:event_index'))
    else:
        context = {
            'failed': False
        }
        return render(request, 'app/create_event.html', context)


def register(request, event_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_detail'))
    event = get_object_or_404(Event, pk=event_id)
    attendees = RegisteredEvents.objects.filter(event=event)
    # adds event to list of registered events
    if RegisteredEvents.objects.filter(event=event, user=request.user).exists():
        context = {
            'event': event,
            'error_message': "Already registered!",
            'attendees': attendees
        }
        return render(request, 'app/event_detail.html', context)
    registered_event = RegisteredEvents(event=event, user=request.user)
    registered_event.save()
    context = {
        'event': event,
        'error_message': "Successfully registered!",
        'attendees': attendees
    }
    return render(request, 'app/event_detail.html', context)


def unregister(request, event_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    event = get_object_or_404(Event, pk=event_id)
    # removes event from list of registered events
    RegisteredEvents.objects.filter(event=event, user=request.user).delete()
    return HttpResponseRedirect(reverse('app:profile'))


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:event_index'))
    registered_events = RegisteredEvents.objects.filter(user=request.user)
    created_events = CreatedEvents.objects.filter(user=request.user)
    context = {
        'registered_events': registered_events,
        'created_events': created_events
    }
    return render(request, 'app/profile.html', context)


def search(request):
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        events_check_info = Event.objects.filter(info__icontains=query_string)
        events_check_title = Event.objects.filter(title__icontains=query_string)
        events_check_date = Event.objects.filter(day__icontains=query_string)
        events_check_location = Event.objects.filter(location__icontains=query_string)
        events = events_check_info | events_check_title | events_check_date | events_check_location
        return render(request, 'app/event_index.html', {'events': events})
    else:
        events = Event.objects.all()
        return render(request, 'app/event_index.html', {'events': events})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:event_index'))


