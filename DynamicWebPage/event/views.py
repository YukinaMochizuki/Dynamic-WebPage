from event.models import Event
from event.serializers import EventSerializer

from rest_framework import viewsets
from rest_framework import generics

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        accountnameArgs = self.kwargs['accountname']
        eventTypeArgs = self.kwargs['eventType']
        return Event.objects.filter(eventType=eventTypeArgs, owner=accountnameArgs)