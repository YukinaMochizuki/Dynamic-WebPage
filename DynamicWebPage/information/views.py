from information.models import Information
from information.serializers import InformationSerializer

from rest_framework import viewsets

class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer