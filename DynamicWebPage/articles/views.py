# Create your views here.

from articles.models import Kanban, Article
from articles.serializers import KanbanSerializer, ArticleSerializer

from DynamicWebPage.SessionAuthentication import CsrfExemptSessionAuthentication, BasicAuthentication

from rest_framework import viewsets

class KanbanViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

