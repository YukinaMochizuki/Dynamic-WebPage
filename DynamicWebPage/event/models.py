import uuid
from django.db import models

# Create your models here.

class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField(max_length=100)
    creareDate = models.DateTimeField(auto_now_add=True)
    lastEditDate = models.DateTimeField(auto_now=True)

    eventType = models.CharField(max_length=100)
    context = models.TextField()
    status = models.TextField()
    
    def __str__(self):
        return "%s" % (self.context)

    class Meta:
        db_table = "event"
