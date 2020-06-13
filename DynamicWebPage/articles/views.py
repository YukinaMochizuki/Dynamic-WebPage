# Create your views here.

from articles.models import Kanban, Article
from articles.serializers import KanbanSerializer, ArticleSerializer

from rest_framework import viewsets

class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
