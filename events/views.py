from django.shortcuts import render
from events.models import Banner

# Create your views here.
def events_list(request):
    images = Banner.objects.all()
    if request.method == "GET":
        event = request.GET.get('event')
        print(event)
        return render(
            request,
            'events/list_events.html'
        )