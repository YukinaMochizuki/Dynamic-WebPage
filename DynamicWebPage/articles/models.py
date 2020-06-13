import uuid
from django.db import models

# Create your models here.

class Kanban(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.URLField(blank=True)
    
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = "kanban"

class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField(max_length=100)
    lastEditAccount = models.CharField(max_length=100)
    creareDate = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now=True)

    title = models.TextField()
    coverImage = models.URLField(blank=True)
    content = models.TextField(blank=True)
    
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        db_table = "article"