from account.models import Account
from account.serializers import AccountSerializer

from DynamicWebPage.SessionAuthentication import CsrfExemptSessionAuthentication, BasicAuthentication

from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
