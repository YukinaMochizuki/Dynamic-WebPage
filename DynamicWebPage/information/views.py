from information.models import Information
from information.serializers import InformationSerializer

from DynamicWebPage.SessionAuthentication import CsrfExemptSessionAuthentication, BasicAuthentication

from rest_framework import viewsets

class InformationViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    queryset = Information.objects.all()
    serializer_class = InformationSerializer