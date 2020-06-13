from rest_framework import serializers
from articles.models import Kanban, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = '__all__'

