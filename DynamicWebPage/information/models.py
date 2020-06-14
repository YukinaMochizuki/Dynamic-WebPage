import uuid
from django.db import models

# Create your models here.

class Information(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    coverImage = models.URLField(blank=True)
    content = models.TextField(blank=True)
    
    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        db_table = "information"